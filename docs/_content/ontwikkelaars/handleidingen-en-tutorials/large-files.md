---
title: "Large files upload tutorial"
weight: 100
---

In this tutorial we explore the ways to upload files to DRC depending on the file size. 

The most relevant component for this tutorial:

* DRC: for creating documents and uploading files

## The requirements for this tutorial

* `docker` and `docker-compose` to host the components locally on your (development machine). 
  See [installatie en configuratie](./installatie-en-configuratie) for a detailed description.
* The [eenmalige setup](./eenmalige-setup) has been carried out.

## Overview of file upload process in DRC

The main resource of DRC API is `EnkelvoudigInformatieObject` which supports creating and editing documents. 
It's content can be divided into metadata (`identificatie`, `creatiedatum`, `titel` and etc) and file content.
The main metadata of file content used by DRC is file size derived from `bestandsomvang` attribute. 
The process of uploading files is chosen based on the comparision of the value of `bestandsomvang` and the maximum file size.

There can be 3 options:

* file size = 0, i.e. document contains only metadata without file content. Document is created during 1 request to DRC.
* file size <= maximum size. In this case file content is expected to be in `inhoud` attribute in 1 request.
* file size > maximum size. In this case file content should be divided by parts and each part should be upload in the separate request.

## To work

In this tutorial we will consider all three ways to create document base on the files size.

### Configure Maximujm file size

The process choice depends on maximum file size. 
The default value of this parameter = 4GB (or 4294967296 Bytes)

### Configure ZTC

Creation documents require the link to `informatieobjecttype`. 
Therefore before creating documents we need to create `informatieobjecttype` 

Open in your browser `http://<ztc-ip>:8002/admin/` and log in with your username and password. 
The API address is from ['installatie en configuratie'](./installatie-en-configuratie) tutorial.

#### Create Catalogus

`Catalogus` represents the collection of `informatieobjecttype` and other objects.

1. Navigate to **Catalogussen** and click on **Toevoegen**.
2. Fill in all the required fields
3. Click on **Opslaan en opnieuw bewerken**.

#### Create Informatieobjecttype

1. Navigate to **Informatieobjecttypen** and click on **Toevoegen**.
2. Fill in all the required fields
3. Click on **Opslaan en opnieuw bewerken**.

#### Request Informatieobjecttype
In previous part we have created an Informatieobjecttype. We request it now to have the url of Informatieobjecttype.

   Get `Catalogussen`:

   ```http
   GET http://<ztc-ip>:8002/api/v1/catalogussen HTTP/1.0
   Authorization: Bearer abcd1234
   ```

   Example response:

   ```json
   [
      {
          "url": "<catalogus url>",
          "domein": "DEMO",
          "rsin": "123456782",
          "contactpersoonBeheerNaam": "VNG API-lab",
          "contactpersoonBeheerTelefoonnummer": "+31 (0)20 123 45 67",
          "contactpersoonBeheerEmailadres": "vngapilab@example.com",
          "zaaktypen": [],
          "besluittypen": [],
          "informatieobjecttypen": [
              "<informatieobjecttype url>" 
          ]
      }
   ]
   ```

Now we have `informatieobjecttype url` which we will use in the next step

### Create document

Now we will create document with 3 different ways to upload files.  

#### Create document without file. 

To create a document only with metadata we need:

* leave `inhoud` field empty
* `bestandsomvang` = 0 

    Example request:

    ```http
    POST http://<drc-ip>:8000/api/v1/enkelvoudiginformatieobjecten HTTP/1.0
    Authorization: Bearer abcd1234
    Content-Type: application/json
   
    {
        "identificatie": "12345",
        "bronorganisatie": "123456782",
        "creatiedatum": "2019-06-27",
        "titel": "detailed summary",
        "auteur": "document auteur",
        "taal": "eng",
        "bestandsomvang": 0,
        "bestandsnaam": "file_name",
        "informatieobjecttype": "<informatieobjecttype url>",
        "vertrouwelijkheidaanduiding": "openbaar"
    }
    ``` 
    
The response contains the created document without lock. 

#### Create document with small file

To create the document with file size less or equal maximum file size we need:

* encode file content to Base64 and place it into `inhoud` attribute.
* `bestandsomvang` = the actual size of file

    Example request:

    ```http
    POST http://<drc-ip>:8000/api/v1/enkelvoudiginformatieobjecten HTTP/1.0
    Authorization: Bearer abcd1234
    Content-Type: application/json
    
    {
        "identificatie": "12345",
        "bronorganisatie": "123456782",
        "creatiedatum": "2019-06-27",
        "titel": "detailed summary",
        "auteur": "document auteur",
        "taal": "eng",
        "bestandsomvang": 17,
        "bestandsnaam": "file_name",
        "inhoud": "c29tZSBmaWxlIGNvbnRlbnQ=",
        "informatieobjecttype": "<informatieobjecttype url>",
        "vertrouwelijkheidaanduiding": "openbaar"
    }
    ``` 

The document is created without lock   
The response contains the url to download the file in `inhoud` attribute. 
   
#### Create document with large file   

To create the document with file size larger than maximum file size we need to perform several requests

1. Create document with specified file size
    
    * leave `inhoud` field empty
    * `bestandsomvang` = total file size 

    ```http
    POST http://<drc-ip>:8000/api/v1/enkelvoudiginformatieobjecten HTTP/1.0
    Authorization: Bearer abcd1234
    Content-Type: application/json
   
    {
        "identificatie": "12345",
        "bronorganisatie": "123456782",
        "creatiedatum": "2019-06-27",
        "titel": "detailed summary",
        "auteur": "document auteur",
        "taal": "eng",
        "bestandsomvang": 5000000000,
        "bestandsnaam": "file_name",
        "informatieobjecttype": "<informatieobjecttype url>",
        "vertrouwelijkheidaanduiding": "openbaar"
    }
    ``` 

    The created document is locked, which means that only users with lock key can change it. 
    The response contains this lock key and `bestandsdelen` part with information for file parts uploading. 
    
    Part of example response:

    ```json
    {
        "url": "http://<drc-ip>:8000/api/v1/enkelvoudiginformatieobjecten/<uuid>",
        ...
        "bestandsomvang": 5000000000,
        "locked": true,
        "bestandsdelen": [
            {
                "url": "http://<drc-ip>:8000/api/v1/bestandsdelen/<uuid1>",
                "volgnummer": 1,
                "omvang": 4294967296,
                "voltooid": false
            },
            {
                "url": "http://<drc-ip>:8000/api/v1/bestandsdelen/<uuid2>",
                "volgnummer": 2,
                "omvang": 705032704,
                "voltooid": false
            }
        ],
        "lock": "abcd"
    }
    ```

    Each of `bestandsdelen` object includes information necessary for upload of file parts:
    
    * `url`: the link for uploading the file part
    * `volgnummer`: the sequence number of this part. The order of merging file parts after their upload depends on this attribute.
    * `omvang`: the size of the file part in Bytes
    * `voltooid`: status it this file part is uploaded yet. 

2. Upload file parts

    Now we need to split our file into file parts such as their size would match the sizes of `bestandsdelen` objects.
    
    After splitting the file we need to upload each file part in the separate request
    Each request should be in multipart format and have following data:
    
    * `lock`: lock key, which was received in the previous step
    * `inhoud`: part file content in binary format
    
    The example request in Postman:
    ![postman_multipart](./_assets/postman_multipart.png)
    
    In the result `voltooid` should be changed to "true".

3. Unlock the document

    After uploading all the parts it is time to unlock the document. 
    By unlocking the user shows that the uploading process is finished and the file can be gathered together from uploaded file parts.

    ```http
    POST http://<drc-ip>:8000/api/v1/enkelvoudiginformatieobjecten/<uuid>/unlock HTTP/1.0
    Authorization: Bearer abcd1234
    Content-Type: application/json

    {
        "lock": "abcd"
    }
    ```

    During unlock all file parts were merged into the whole file, all temporary file parts were removed.
    
4. Request the document

    We can request the created document to see the changes.

    ```http
    GET http://<drc-ip>:8000/api/v1/enkelvoudiginformatieobjecten/<uuid> HTTP/1.0
    Authorization: Bearer abcd1234
    Content-Type: application/json
    ```

    Part of the example response:

    ```json
    {
        "url": "http://<drc-ip>:8000/api/v1/enkelvoudiginformatieobjecten/<uuid>",
        ...
        "inhoud": "http://<drc-ip>:8000/api/v1/enkelvoudiginformatieobjecten/<uuid>/download?versie=1",
        "locked": false,
        "bestandsdelen": []
    }
    ```
    Now the document is unlocked, all `bestandsdelen` are removed and the file content can be download via the `inhoud` url
 

###Summary
In this tutorial in ZTC we:

* created Catalogus;
* created Informatieobjecttype 

After that we explore 3 options to create a document in DRC:
* without a file
* with the small file
* with the large file (multiple step approach)
