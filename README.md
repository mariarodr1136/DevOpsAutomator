# DevOps Automation Scripts

This project demonstrates the use of automation scripts, containerization with Docker, container orchestration with Kubernetes, and infrastructure provisioning using Terraform.

![Python](https://img.shields.io/badge/Python-3.8-blue) ![Bash](https://img.shields.io/badge/Bash-Shell-orange) ![Docker](https://img.shields.io/badge/Docker-Container-blue) ![Kubernetes](https://img.shields.io/badge/Kubernetes-Container%20Orchestration-green) ![Terraform](https://img.shields.io/badge/Terraform-Infrastructure%20as%20Code-red) ![AWS](https://img.shields.io/badge/AWS-Cloud-yellow) ![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Container%20Management-lightblue)

--- 

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Features](#features)
3. [Getting Started](#getting-started)
    1. [Clone the Repository](#1-clone-the-repository)
    2. [Ensure Prerequisites are Met](#2-ensure-prerequisites-are-met)
        1. [Docker](#21-docker)
        2. [Kubernetes (Minikube or kubeadm)](#22-kubernetes-minikube-or-kubeadm)
        3. [Terraform](#23-terraform)
        4. [AWS CLI (Optional, for AWS infrastructure)](#24-aws-cli-optional-for-aws-infrastructure)
        5. [Python (for Python automation scripts)](#25-python-for-python-automation-scripts)
        6. [Docker Compose](#26-docker-compose)
    3. [Setup Instructions](#3-setup-instructions)
        1. [Build Docker Images](#31-build-docker-images)
        2. [Configure Kubernetes](#32-configure-kubernetes)
        3. [Initialize Terraform](#33-initialize-terraform)
        4. [Run the Automation Script](#34-run-the-automation-script)
        5. [Access Your Application](#35-access-your-application)
4. [Notes](#notes)
5. [Troubleshooting](#troubleshooting)
6. [Contributing](#contributing)
7. [Contact](#contact-)

---

## Technologies Used
- Python/Bash
- Docker
- Kubernetes
- Terraform

## Features
- Automated deployment pipeline with Python or Bash scripts
- Docker containerization for applications
- Kubernetes deployment and service configuration
- Terraform infrastructure provisioning

---

## Getting Started

### 1. Clone the repository
git clone https://github.com/mariarodr1136/DevOpsAutomator.git
cd DevOpsAutomator

### 2. Ensure prerequisites are met
Before running the scripts, make sure the following tools are installed and configured on your machine:

#### 2.1 Docker
Docker is required for containerization and managing application deployment.
- [Install Docker](https://docs.docker.com/get-docker/)
- Verify installation:
docker --version

#### 2.2 Kubernetes (Minikube or kubeadm)
Kubernetes is used for orchestrating containers in the deployment.
- Install Minikube
- Verify installation:
kubectl version --client

#### 2.3 Terraform
Terraform is used for provisioning infrastructure on cloud platforms.
- Install Terraform
- Verify installation:
terraform --version

#### 2.4 AWS CLI (Optional, for AWS infrastructure)
If using AWS as the provider for Terraform, configure the AWS CLI.
- Install AWS CLI
- Configure AWS CLI:
aws configure

#### 2.5 Python (for Python automation scripts)
If using Python automation scripts, make sure Python 3 is installed.
- Install Python
- Verify installation:
python3 --version

#### 2.6 Docker Compose
Docker Compose is used to manage multi-container Docker applications.
- Install Docker Compose
- Verify installation:
docker-compose --version

---

## 3. Setup Instructions

#### 3.1 Build Docker images
To build the Docker image, navigate to the Docker directory and use the docker-compose command:
docker-compose build

#### 3.2 Configure Kubernetes
Ensure that your Kubernetes cluster is up and running. You can use Minikube or a managed Kubernetes service like GKE or EKS.

For Minikube:
minikube start
kubectl config use-context minikube

#### 3.3 Initialize Terraform
If you're provisioning infrastructure on AWS or another cloud provider, navigate to the Terraform directory and initialize Terraform:
cd Terraform
terraform init

#### 3.4 Run the Automation Script
To deploy your application and provision the infrastructure, you can either use the Python or Bash script.

- Using Python:
python3 Scripts/deploy_pipeline.py

- Using Bash:
bash Scripts/provision_infrastructure.sh

#### 3.5 Access Your Application
Once the deployment is complete, you can access your application depending on how the Kubernetes services are configured:

- If you're using a LoadBalancer type service, check the external IP:
kubectl get services

- If you're using Minikube, you can access the application through the Minikube service URL:
minikube service myapp-service --url

## Notes

- The Terraform script currently provisions an EC2 instance in AWS. Modify the main.tf file for additional infrastructure setups (e.g., VPC, S3, etc.).
- The Kubernetes configurations are set for a basic app deployment, but you can modify the deployment.yaml to include environment variables, secrets, or additional configurations like autoscaling.
- Docker Compose is set to run the containerized app on localhost:5000. Modify the ports in the docker-compose.yml file if needed.

---

## Troubleshooting

- Docker errors: If you encounter issues with Docker, ensure that Docker is running and properly configured. 
  - Check Docker logs for more details:
docker logs <container_id>

- Kubernetes errors: Check the status of Kubernetes pods and services with:
kubectl get pods
kubectl get services

- Terraform errors: Terraform errors can often be related to missing provider credentials or syntax issues in the .tf files. Ensure your credentials are configured correctly and try re-running the Terraform commands.

---

## Contributing 
Feel free to submit issues or pull requests for improvements or bug fixes. You can also open issues to discuss potential changes or enhancements. All contributions are welcome to enhance the app’s features or functionality!

To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feat/your-feature-name
- Alternatively, for bug fixes:
   ```bash
   git checkout -b fix/your-bug-fix-name
3. Make your changes and run all tests before committing the changes and make sure all tests are passed.
4. After all tests are passed, commit your changes with descriptive messages:
   ```bash
   git commit -m 'add your commit message'
5. Push your changes to your forked repository:
   ```bash
   git push origin feat/your-feature-name.
6. Submit a pull request to the main repository, explaining your changes and providing any necessary details.

---

### Contact 🌐
If you have any questions or feedback, feel free to reach out at [mrodr.contact@gmail.com](mailto:mrodr.contact@gmail.com).
