from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "deploy_bot.utils"

    def ready(self):
        from . import checks  # noqa
