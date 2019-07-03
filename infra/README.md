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


## Kubenetes layout

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

TODO

### Database

There is a single, postgis-enabled database cluster. The layout is described
in `k8s/database`.

To deploy these, run:

```bash
kubectl -n zgw apply k8s/database/
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

For each service (ZRC, DRC, ZTC, BRC, NRC, AC), you deploy them using:

```bash
kubectl -n zgw apply k8s/<lower-cased-service>/
```

e.g.:

```bash
kubectl -n zgw apply k8s/zrc/
```

### Documentation

```bash
kubectl -n zgw apply k8s/docs/
```

### Referentielijsten/Gemeentelijke Selectielijst

```bash
kubectl -n zgw apply k8s/vrl/
```

### Deploy bot

The deploy bot is a service account running the cluster that can manage other
deployments (such updating to newer images).

Create the service account with the required roles:

```bash
kubectl -n zgw apply k8s/deploy/
```

### NLX inway

```bash
kubectl -n zgw apply k8s/inway/
```

### Token tool

```bash
kubectl -n zgw apply k8s/tokens/
```

### Redirects for previous domain

```bash
kubectl -n zgw apply k8s/old_domain/
```

### Ingress

WARNING: do not deploy new domains in the ingress if the DNS is not properly
set up/stable yet! This will cause issues with the LetsEncrypt certificates.

```bash
kubectl -n zgw apply k8s/ingress.yml
```
