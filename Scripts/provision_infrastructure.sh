#!/bin/bash

# Provision Docker containers
docker-compose up -d

# Apply Kubernetes configurations
kubectl apply -f Kubernetes/

# Provision infrastructure using Terraform
terraform init
terraform apply -auto-approve
