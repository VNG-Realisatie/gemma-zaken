import logging

from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from .validators import ImageValidator

logger = logging.getLogger(__name__)


class DeploymentSerializer(serializers.Serializer):
    """
    Specify what should be deployed.
    """

    name = serializers.CharField(label=_("name"), help_text=_("Name of the deployment"))
    namespace = serializers.CharField(
        label=_("namespace"), help_text=_("Namespace where the deployment lives")
    )
    container_name = serializers.CharField(
        label=_("container name"), help_text=_("Name of the container to update")
    )
    image = serializers.CharField(
        label=_("image"),
        help_text=_("Image to deploy, including tag"),
        validators=[ImageValidator()],
    )
