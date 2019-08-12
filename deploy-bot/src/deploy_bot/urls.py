from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView

handler500 = "deploy_bot.utils.views.server_error"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("deploy_bot.api.urls")),

    # Simply show the API docs.
    path("", RedirectView.as_view(url=reverse_lazy("schema-redoc", kwargs={"version": 1}))),
    path("ref/", include("vng_api_common.urls")),
]

# NOTE: The staticfiles_urlpatterns also discovers static files (ie. no need to run collectstatic). Both the static
# folder and the media folder are only served via Django if DEBUG = True.
urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
