import logging

from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import DeploymentSerializer

logger = logging.getLogger(__name__)


class DeploymentViewSet(viewsets.ViewSet):
    """
    Describe viewset.

    create:
    Trigger a deployment.
    """

    def create(self, request, *args, **kwargs):
        serializer = DeploymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
