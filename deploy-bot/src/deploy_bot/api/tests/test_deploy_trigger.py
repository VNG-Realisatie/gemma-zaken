from unittest.mock import patch

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from vng_api_common.tests import reverse

from deploy_bot.accounts.models import User


@patch("deploy_bot.api.viewsets.deploy")
class DeploymentTests(APITestCase):
    def setUp(self):
        super().setUp()
        user = User.objects.create_user("jenkins")
        token = Token.objects.create(user=user)

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_trigger_deploy(self, mock_deploy):
        url = reverse("deployment-list")

        body = {
            "name": "zrc",
            "namespace": "zgw",
            "container_name": "zrc",
            "image": "vngr/gemma-zrc:latest",
        }
        response = self.client.post(url, body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        mock_deploy.assert_called_once_with(
            name="zrc",
            namespace="zgw",
            container_name="zrc",
            image="vngr/gemma-zrc:latest",
        )
