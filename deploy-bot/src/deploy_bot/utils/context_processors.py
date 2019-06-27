from django.conf import settings as django_settings


def settings(request):
    public_settings = (
        "GOOGLE_ANALYTICS_ID",
        "ENVIRONMENT",
        "SHOW_ALERT",
        "PROJECT_NAME",
    )

    return {
        "settings": dict(
            [(k, getattr(django_settings, k, None)) for k in public_settings]
        )
    }
