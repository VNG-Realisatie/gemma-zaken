from vng_api_common.conf.api import *  # noqa - imports white-listed

REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()
REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = (
    "rest_framework.authentication.TokenAuthentication",
    "rest_framework.authentication.SessionAuthentication",
)

SECURITY_DEFINITION_NAME = "Authtoken"

SWAGGER_SETTINGS = BASE_SWAGGER_SETTINGS.copy()

_default_field_inspectors = list(BASE_SWAGGER_SETTINGS["DEFAULT_FIELD_INSPECTORS"])
_default_field_inspectors.remove(
    "vng_api_common.inspectors.geojson.GeometryFieldInspector"
)

SWAGGER_SETTINGS.update(
    {
        "DEFAULT_INFO": "deploy_bot.api.schema.info",
        "SECURITY_DEFINITIONS": {
            SECURITY_DEFINITION_NAME: {
                # OAS 3.0
                "type": "apiKey",
                "in": "header",
                "name": "Authorization",
                # not official...
                # Swagger 2.0
                # 'name': 'Authorization',
                # 'in': 'header'
                # 'type': 'apiKey',
            }
        },
        "DEFAULT_FIELD_INSPECTORS": tuple(_default_field_inspectors),
    }
)

GEMMA_URL_INFORMATIEMODEL_VERSIE = "1.0"
