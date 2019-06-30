import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from deploy_bot.k8s import deploy

from .serializers import DeploymentSerializer

logger = logging.getLogger(__name__)


class DeploymentViewSet(viewsets.ViewSet):
    """
    Describe viewset.

    create:
    Trigger a deployment.
    """

    @swagger_auto_schema(request_body=DeploymentSerializer)
    def create(self, request, *args, **kwargs):
        serializer = DeploymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        deploy(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
