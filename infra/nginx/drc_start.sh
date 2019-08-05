#!/bin/bash

set -ex

# template out proxy config
envsubst '$$DRC_HOST,$$DRC_UWSGI_PORT' \
    < /etc/nginx/conf.d/proxy.template \
    > /etc/nginx/conf.d/proxy

# template out server config
envsubst '$$DRC_NGINX_PORT,$$MIN_UPLOAD_SIZE' \
    < /etc/nginx/conf.d/mysite.template \
    > /etc/nginx/conf.d/default.conf

# start nginx in the foreground
exec nginx -g 'daemon off;'
