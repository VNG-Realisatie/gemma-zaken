# Infrastructure

The aim of this document is to describe on which infrastructure we deploy and
how to manage it. Familiarity with Ansible and Kubernetes are assumed.

Haven is the project/platform running on Kubernetes where applications can be
deployed. This project is deployed in the `zgw` namespace.

## Requirements

* `kubectl` binary on your system
* access to the Haven bastion (IP-address white list), possibly through a jump host
* kube config file for the Haven cluster
* Ansible vault installation (see `requirements.txt`)
* `openshift` - best to specify the python interpreter in the `hosts` file
  to point to your virtualenv with Ansible.
* Ansible Vault password if you're touching secrets

## Preparation

### Requesting access to the k8s cluster

Follow the steps [here](https://auth.common.haven.vng.cloud/) to setup your local workspace to connect with the Haven cluster. Your IP address also has to be whitelisted in order to continue with the next steps.

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

Note that (most of) the YAML files are _templates_ for Ansible.

### Secrets

The raw values for secrets are Ansible-vault encrypted. This means you need
to provide the Ansible-vault password during deployment.

All secrets in K8S are managed via Ansible to facilitate templating and proper
INFOSEC practices.

* `ansible/vars/secrets.yml` contains the secrets for the stable environment
* `ansible/vars/secrets-test.yml` contains the secrets for the testing environment

### Deploying the test environments

The testing environments are running the latest versions of each component,
usually based off the `develop` branch.

Deploy using Ansible:

```bash
ansible-playbook deploy-test.yml --ask-vault-pass
```

Configuration of each service is defined in `vars/test.yml`.

### Deploying the stable environments

The stable environments are running the stable versions of each component,
based off the release tags on the `master` branch.

Deploy using Ansible:

```bash
ansible-playbook deploy-stable.yml --ask-vault-pass
```

Configuration of each service is defined in `vars/stable.yml`.

### Database

There is a single, postgis-enabled database cluster. The layout is described
in `k8s/database`.

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

Deploy these using the Ansible playbooks (stable or test).

### Documentation

```bash
kubectl -n zgw apply -f k8s/docs/
```

### Deploy bot

The deploy bot is a service account running the cluster that can manage other
deployments (such updating to newer images).

The secrets are managed with the `deploy-stable.yml` playbook.

After running the stable playbook, create the service account with the required
roles and deploy the web API:

```bash
kubectl -n zgw apply -f k8s/deploy/rbac.yaml
kubectl -n zgw apply -f k8s/deploy/web.yml
```

### NLX inway

The secrets are managed with the `deploy-stable.yml` playbook.

```bash
kubectl -n zgw apply -f k8s/inway/inway.yml
```

### Token tool

The secrets are managed with the `deploy-stable.yml` playbook.

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
