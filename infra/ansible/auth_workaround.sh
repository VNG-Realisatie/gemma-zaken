# Workaround for Pinniped login on the cluster, since the OpenShift k8s client
# used by Ansible does not support this auth mechanism

# EXAMPLE USAGE:
# $ source ./auth_workaround.sh
# $ ansible-playbook deploy-stable.yml --ask-vault-pass

mkdir -p ~/.tmp

CA_DATA=$(kubectl config view --raw -o jsonpath='{.clusters[?(@.name=="azure-common-prod")].cluster.certificate-authority-data}')
SERVER=$(kubectl config view --raw -o jsonpath='{.clusters[?(@.name=="azure-common-prod")].cluster.server}')

pinniped login oidc \
      --enable-concierge \
      --concierge-authenticator-name=haven-authenticator \
      --concierge-authenticator-type=jwt \
      --concierge-endpoint=$SERVER \
      --concierge-ca-bundle-data=$CA_DATA \
      --issuer=https://supervisor.haven.vng.cloud \
      --request-audience=common.haven.vng.cloud \
      --upstream-identity-provider-name=dex > ~/.tmp/pinniped-creds.json

cat ~/.tmp/pinniped-creds.json | jq -j '.status.clientKeyData' > ~/.tmp/client.key
cat ~/.tmp/pinniped-creds.json | jq -j '.status.clientCertificateData' > ~/.tmp/client.crt

chmod 0600 ~/.tmp/*

export K8S_AUTH_CERT_FILE=~/.tmp/client.crt
export K8S_AUTH_KEY_FILE=~/.tmp/client.key
