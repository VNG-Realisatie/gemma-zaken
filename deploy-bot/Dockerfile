# Stage 1 - Compile needed python dependencies
FROM python:3.6-alpine AS build
RUN apk --no-cache add \
    gcc \
    musl-dev \
    pcre-dev \
    linux-headers \
    postgresql-dev \
    python3-dev \
    # libraries installed using git
    git \
    # lxml dependencies
    libxslt-dev \
    # pillow dependencies
    jpeg-dev \
    openjpeg-dev \
    zlib-dev

WORKDIR /app

COPY ./requirements /app/requirements
RUN pip install pip setuptools -U
RUN pip install -r requirements/production.txt


# # Stage 2 - build frontend
# FROM mhart/alpine-node:10 AS frontend-build

# WORKDIR /app

# COPY ./*.json /app/
# RUN npm install

# COPY ./Gulpfile.js /app/
# COPY ./build /app/build/

# COPY src/deploy_bot/sass/ /app/src/deploy_bot/sass/
# RUN npm run build


# # Stage 3 - Prepare jenkins tests image
# FROM build AS jenkins

# RUN apk --no-cache add \
#     postgresql-client

# # Stage 3.1 - Set up the needed testing/development dependencies
# COPY --from=build /usr/local/lib/python3.6 /usr/local/lib/python3.6
# COPY --from=build /app/requirements /app/requirements

# RUN pip install -r requirements/jenkins.txt --exists-action=s

# # Stage 3.2 - Set up testing config
# COPY ./setup.cfg /app/setup.cfg
# COPY ./bin/runtests.sh /runtests.sh

# # Stage 3.3 - Copy source code
# COPY ./src /app/src
# CMD ["/runtests.sh"]


# Stage 4 - Build docker image suitable for execution and deployment
FROM python:3.6-alpine AS production
RUN apk --no-cache add \
    ca-certificates \
    mailcap \
    musl \
    pcre \
    postgresql \
    # lxml dependencies
    libxslt \
    # pillow dependencies
    jpeg \
    openjpeg \
    zlib

# Stage 4.1 - Set up dependencies
COPY --from=build /usr/local/lib/python3.6 /usr/local/lib/python3.6
COPY --from=build /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# Stage 4.2 - Copy source code
WORKDIR /app
COPY ./bin/docker_start.sh /start.sh
RUN mkdir /app/log

COPY ./src /app/src

ENV DJANGO_SETTINGS_MODULE=deploy_bot.conf.docker

ARG SECRET_KEY=dummy

# Run collectstatic, so the result is already included in the image
RUN python src/manage.py collectstatic --noinput

EXPOSE 8000
CMD ["/start.sh"]
