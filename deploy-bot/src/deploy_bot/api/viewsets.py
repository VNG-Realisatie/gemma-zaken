import logging

from rest_framework import viewsets
from vng_api_common.permissions import ActionScopesRequired

from .scopes import EXAMPLE_SCOPE
from .serializers import ExampleSerializer

logger = logging.getLogger(__name__)


class ExampleViewSet(viewsets.ModelViewSet):
    """
    Describe viewset.

    create:
    Describe create operation.

    list:
    Describe list operation.

    partial_update:
    Describe partial_update operation.

    destroy:
    Describe destroy operation.
    """

    queryset = ...
    serializer_class = ExampleSerializer
    lookup_field = "uuid"

    permission_classes = (ActionScopesRequired,)
    required_scopes = {
        "list": EXAMPLE_SCOPE,
        "retrieve": EXAMPLE_SCOPE,
        "create": EXAMPLE_SCOPE,
        "update": EXAMPLE_SCOPE,
        "partial_update": EXAMPLE_SCOPE,
        "destroy": EXAMPLE_SCOPE,
    }
