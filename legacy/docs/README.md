# GEMMA Zaken &middot; Documentatie website

De documentatie website is het startpunt voor iedereen die iets wil gaan doen
met GEMMA Zaken.


## Bijdragen

Alle bijdragen zijn welkom middels
[Pull Requests](https://github.com/VNG-Realisatie/gemma-zaken/pulls). Alle
documentatie is opgemaakt in
[MarkDown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
en bevindt zich in de `docs/content` directory van deze repository.

Elk bestand moet starten met een
[Hugo front-matter](https://gohugo.io/content-management/front-matter/) deel.


## Ontwikkelaars

De documentatie van deze website wordt automatisch gegenereerd op basis van de
bestanden in deze repository.

Om snel aan de slag te gaan:

1. Download en installeer [Jekyll](https://jekyllrb.com/).

2. Clone de [GEMMA Zaken](https://github.com/VNG-Realisatie/gemma-zaken)
   repository.
   ```bash
   $ git clone git@github.com:VNG-Realisatie/gemma-zaken.git
   ```

3. Ga naar de `docs` directory en start `jekyll serve`.
   ```bash
   cd docs
   $ bundle exec jekyll serve
   ```

## Docker

Om de documentatie website via [Docker](https://docs.docker.com/) te draaien:

1. Bouw en start de Docker container.
   ```bash
   $ cd docs
   $ ./release-docker-image.sh
   $ docker run -p 80:80 --rm --name gemma-zaken-docs vngr/gemma-zaken-docs
   ```

2. De documentatie is nu beschikbaar op `http://localhost/`.

   Indien `Docker Machine` wordt gebruikt, moet je verbinden met het IP van de
   Docker VM. Je kan dit IP opvragen door `docker-machine ls` uit te voeren en
   in de browser `http://<ip>/` in te tikken (waar het `<ip>` gelijk is aan
   het IP in de URL kolom):
   ```bash
   $ docker-machine ls
   NAME      ACTIVE   DRIVER       STATE     URL
   default   *        virtualbox   Running   tcp://<ip>:<port>
   ```

3. Om de docker container te stoppen:
   ```bash
   $ docker stop gemma-zaken-docs
   ```
