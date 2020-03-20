FROM ruby:2.6.1-alpine AS build

# Install build tools.
RUN apk add build-base zlib-dev

WORKDIR /app

COPY _config.yml Gemfile Gemfile.lock ./

RUN gem install jekyll bundler && \
    bundle install && \
    rm -rf public

COPY . /app

RUN bundle exec jekyll build

# Copy static docs to alpine-based nginx container.
FROM nginx:stable-alpine

# Copy nginx configuration
COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/_site /usr/share/nginx/html
COPY ./api-specificatie /usr/share/nginx/html
