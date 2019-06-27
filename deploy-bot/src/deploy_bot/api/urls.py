from django.conf.urls import url
from django.urls import include

from vng_api_common import routers
from vng_api_common.schema import SchemaView

from .viewsets import DeploymentViewSet

router = routers.DefaultRouter()
router.register("deployments", DeploymentViewSet, base_name="deployment")


# TODO: the EndpointEnumerator seems to choke on path and re_path

urlpatterns = [
    url(
        r"^v(?P<version>\d+)/",
        include(
            [
                # API documentation
                url(
                    r"^schema/openapi(?P<format>\.json|\.yaml)$",
                    SchemaView.without_ui(cache_timeout=None),
                    name="schema-json",
                ),
                url(
                    r"^schema/$",
                    SchemaView.with_ui("redoc", cache_timeout=None),
                    name="schema-redoc",
                ),
                # actual API
                url(r"^", include(router.urls)),
            ]
        ),
    )
]
