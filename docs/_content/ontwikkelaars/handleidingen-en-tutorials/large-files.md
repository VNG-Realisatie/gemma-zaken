---
title: "Large files upload tutorial"
weight: 100
---

In this tutorial we explore the ways to upload files to DRC depending on the file size. 

The most relevant component for this tutorial:

* DRC: for creating documents and uploading files

## The requirements for this tutorial

* `docker` and `docker-compose` to host the components locally on your (development machine). See 'installation and configuration' for a detailed description.
* The one-time setup has been carried out.

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

The process choice depends on maximum file size. This parameter can be configured as an environment variable `MIN_UPLOAD_SIZE`
For `docker-compose` this variable can be added to `environment` section of `drc nginx` service
The default value of `MIN_UPLOAD_SIZE` = 4GB (or 4294967296 Bytes)

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

   *Example answer*

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

Now we will create 3 documents with different ways to upload files.  

#### 1. Create document without file. 

To create a document only with metadata we need:

* leave `inhoud` field empty
* specify `bestandsomvang` = 0 

Example request:

   ```json
    {
    "identificatie": "12345",
    "bronorganisatie": "123456782",
    "creatiedatum": "2019-06-27",
    "titel": "detailed summary",
    "auteur": "document auteur",
    "taal": "eng",
    "informatieobjecttype": "<informatieobjecttype url>",
    "vertrouwelijkheidaanduiding": "openbaar"
}
``` 

#### 2. Create document with small file

TODO
   
#### 3. Create document with large file   

TODO

http://127.0.0.1:8002/api/v1/informatieobjecttypen/64514464-4c13-41e2-ac66-9b3d445e5e84
