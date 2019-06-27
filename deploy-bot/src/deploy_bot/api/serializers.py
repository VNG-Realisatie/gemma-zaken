import logging

from rest_framework import serializers

logger = logging.getLogger(__name__)


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ...
        fields = ("url", ...)
        extra_kwarsg = {"url": {"lookup_field": "uuid"}}
