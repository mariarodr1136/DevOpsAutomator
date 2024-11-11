#!/bin/bash

# Create the Docker registry secret
kubectl create secret docker-registry docker-registry-secret \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=mariarodr1136 \
  --docker-password=Angiechu1! \
  --docker-email=mrodr.contact@gmail.com

# Provision Docker containers
docker-compose up -d

# Apply Kubernetes configurations
kubectl apply -f Kubernetes/

# Provision infrastructure using Terraform
terraform init
terraform apply -auto-approve