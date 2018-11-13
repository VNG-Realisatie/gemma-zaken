FROM alpine:latest AS build

# Install build tools.
RUN apk add build-base ruby-dev ruby-full zlib-dev

COPY . /app
WORKDIR /app

RUN gem install jekyll bundler && \
    bundler install && \
    rm -rf public && \
    bundle exec jekyll build

# Copy static docs to alpine-based nginx container.
FROM nginx:stable-alpine

# Copy nginx configuration
COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/_site /usr/share/nginx/html
