FROM alpine:latest AS build

# Install build tools.
RUN apk add --update openssl make git

# Install hugo.
RUN wget -O - "https://github.com/gohugoio/hugo/releases/download/v0.36/hugo_0.36_Linux-64bit.tar.gz" | tar --no-same-owner -C /usr/local/bin/ -xz hugo

# Build docs.
COPY . /app
WORKDIR /app
RUN make

# Copy static docs to alpine-based nginx container.
FROM nginx:stable-alpine

# Copy nginx configuration
COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/public /usr/share/nginx/html
