set +x

# Trigger deploy
curl https://deploy-bot-zgw.vng.cloud/api/v1/deployments \
    -H "Authorization: Token ${DEPLOY_BOT_TOKEN}" \
    -H "Content-Type: application/json" \
    --request POST \
    --data @- << EOF

{
    "name":"<TODO>",
    "namespace":"zgw",
    "containerName":"<TODO>",
    "image": "<TODO>"
}
EOF

set -x

echo "Deploy triggered"
