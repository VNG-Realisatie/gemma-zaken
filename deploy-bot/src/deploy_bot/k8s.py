from django.utils import timezone

from kubernetes import client, config


def deploy(name: str, namespace: str, container_name: str, image: str) -> None:
    """
    Patch a deployment `name` to the specified image version

    :param name: Name of the deployment
    :param namespace: Namespace where the deployment exists
    :param container_name: Name of the container to patch
    :param image: Image to update the container to. Format <registry>/<image>:<tag>

    Note that the in-cluster service account and/or the KUBECONFIG file must
    map to a user with permissions to do PATCH operations on the deployment
    resource in the apps api group. For more information, see
    https://kubernetes.io/docs/reference/access-authn-authz/rbac/
    """
    load_config()

    annotations = {"last-deploy": timezone.now().isoformat()}

    apps = client.AppsV1beta1Api()
    apps.patch_namespaced_deployment(
        name,
        namespace,
        {
            "metadata": {"annotations": annotations},
            "spec": {
                "template": {
                    "metadata": {"annotations": annotations},
                    "spec": {"containers": [{"name": container_name, "image": image}]},
                }
            },
        },
    )


def load_config():
    try:
        config.load_incluster_config()
    except config.ConfigException:
        config.load_kube_config()
