from django.conf import settings

from drf_yasg import openapi

description = """An API to trigger deployments.

This API is intended to be consumed by CI such as Jenkins, Travis... It is
notified of new image builds and triggers an in-cluster patch of deployment
objects, leading to new version being deployed.

**Authentication**

You need to be authenticated with an API token to be able to use this API.
You can create an issue on https://github.com/VNG-Realisatie/gemma-zaken for
us to get in touch.
"""

info = openapi.Info(
    title="Deploy Bot API",
    default_version=settings.API_VERSION,
    description=description,
    contact=openapi.Contact(
        email="support@maykinmedia.nl",
        url="https://github.com/VNG-Realisatie/gemma-zaken",
    ),
    license=openapi.License(name="EUPL 1.2"),
)
