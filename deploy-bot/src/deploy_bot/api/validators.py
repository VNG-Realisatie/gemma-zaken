from django.utils.translation import ugettext_lazy as _

from rest_framework.exceptions import ValidationError


class ImageValidator:
    message = _("Invalid image format, expected `<repository>/<image>:<tag>`")
    code = "invalid-image-format"

    def __call__(self, value: str):
        try:
            repo, img = value.split("/")
            image, tag = img.split(":")
        except ValueError:
            raise ValidationError(self.message, code=self.code)
