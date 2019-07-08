# Infrastructure

The aim of this document is to describe on which infrastructure we deploy and
how to manage it. Familiarity with Ansible and Kubernetes are assumed.

Haven is the project/platform running on Kubernetes where applications can be
deployed. This project is deployed in the `zgw` namespace.

## Requirements

* `kubectl` binary on your system
* access to the Haven bastion (IP-address white list), possibly through a jump host
* private key to SSH to Haven bastion
* kube config file for the Haven cluster
* Ansible vault installation (see `requirements.txt`)
* `openshift` - best to specify the python interpreter in the `hosts` file
  to point to your virtualenv with Ansible.
* Ansible Vault password if you're touching secrets

## Preparation

### Setting up the SSH tunnel

Access to the cluster runs through an SSH tunnel.

Directly without jump host:

```bash
ssh -i /path/to/private_key -4 -fNTL \*:6443:10.0.101.9:6443 kubectl@bastion_ip_address
```

With a jump host:

```bash
ssh  -J user@jump-host -i /path/to/private_key -4 -fNTL \*:6443:10.0.101.9:6443 kubectl@bastion_ip_address
```

### Point to the correct kubeconfig

```bash
export KUBECONFIG=/path/to/kube.conf
```

## Deploy to kubernetes cluster

The layout of kubernetes applications is described in YAML format. Important
concepts:

* **Secret**: a secret stores sensitive data such as passwords. They cannot easily
  be read out in graphical interfaces. Secrets can be mounted in containers
  as a volume or provided as environment variables

* **ConfigMap**: similar to secrets, except the data is not sensitive and readable
  in plain text.

* **Volumes**: persistent volumes ensure that stateful data is retained when
  containers are killed/stopped/restarted

* **Deployment**: a template for containers. They describe which volumes apply
  and which containers should run. Kubernetes works towards the desired state,
  e.g. the requested number of replicas

* **Service**: provides a host name and connects to backend containers
  specified in deployments.

* **Ingress**: the public facing entrypoint for traffic. Ingresses match host
  names and paths and point to services to direct traffic to the appropriate
  containers.

### Secrets

The raw values for secrets are Ansible-vault encrypted. This means you need
to provide the Ansible-vault password during deployment.

All secrets in K8S are managed via Ansible to facilitate templating and proper
INFOSEC practices.

```bash
cd ansible
ansible-playbook deploy_secrets.yml --ask-vault-pass
```

### Database

There is a single, postgis-enabled database cluster. The layout is described
in `k8s/database`.

To deploy these, run:

```bash
kubectl -n zgw apply -f k8s/database/postgis.yml
```

Currently only one replica can run with the mounted volume, since volumes
can only be mounted `ReadWriteOnce`.

Once the cluster is initialized, you may need to execute `CREATE DATABASE`
statements.

Get the relevant pod:

```bash
kubectl -n zgw get pods | grep postgis
# postgis-7758497758-tcmgk
```

Get an interactive shell:

```bash
kubectl -n zgw exec -it postgis-7758497758-tcmgk bash
```

Switch to the postgres user and create the database:

```bash
su postgres
createdb DB_NAME
```

### API services

#### ZRC, ZTC, BRC, AC

```bash
kubectl -n zgw apply -f k8s/<lower-cased-service>/web.yml
```

e.g.:

```bash
kubectl -n zgw apply -f k8s/zrc/
```

#### DRC

For the DRC you need some extra yaml files:

```bash
kubectl -n zgw apply -f k8s/drc/volumes.yml
kubectl -n zgw apply -f k8s/drc/web.yml
kubectl -n zgw apply -f k8s/drc/nginx.yml
```

#### NRC

For the NRC you need some extra yaml files:

```bash
kubectl -n zgw apply -f k8s/nrc/celery.yml
kubectl -n zgw apply -f k8s/nrc/rabbitmq.yml
kubectl -n zgw apply -f k8s/nrc/web.yml
```

### Documentation

```bash
kubectl -n zgw apply -f k8s/docs/
```

### Referentielijsten/Gemeentelijke Selectielijst

```bash
kubectl -n zgw apply -f k8s/vrl/web.yml
```

### Deploy bot

The deploy bot is a service account running the cluster that can manage other
deployments (such updating to newer images).

Create the service account with the required roles:

```bash
kubectl -n zgw apply -f k8s/deploy/rbac.yaml
kubectl -n zgw apply -f k8s/deploy/web.yml
```

### NLX inway

```bash
kubectl -n zgw apply -f k8s/inway/inway.yml
```

### Token tool

```bash
kubectl -n zgw apply -f k8s/tokens/web.yml
```

### Redirects for previous domain

```bash
kubectl -n zgw apply -f k8s/old_domain/
```

### Ingress

WARNING: do not deploy new domains in the ingress if the DNS is not properly
set up/stable yet! This will cause issues with the LetsEncrypt certificates.

```bash
kubectl -n zgw apply -f k8s/ingress.yml
```