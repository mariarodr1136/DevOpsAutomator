# DevOps Automation Scripts

This project demonstrates the use of automation scripts, containerization with Docker, container orchestration with Kubernetes, and infrastructure provisioning using Terraform.

## Technologies Used
- Python/Bash
- Docker
- Kubernetes
- Terraform

## Features
- Automated deployment pipeline with Python or Bash scripts
- Docker containerization for application
- Kubernetes deployment and service configuration
- Terraform infrastructure provisioning

## Getting Started
1. Clone the repository
2. Ensure Docker and Kubernetes are installed and configured
3. Run the automation script to deploy the application and provision infrastructure
   - Using Python: `python deploy_pipeline.py`
   - Using Bash: `./provision_infrastructure.sh`

## Prerequisites

Before running the scripts, ensure the following tools are installed and configured on your machine:

### 1. Docker
Docker is required for containerization and managing application deployment.

- [Install Docker](https://docs.docker.com/get-docker/)
- Verify installation with:
  ```bash
  docker --version
2. Kubernetes (Minikube or kubeadm)
Kubernetes is used for orchestrating the containers in the deployment.

Install Minikube
Verify installation with:
kubectl version --client
3. Terraform
Terraform is required for provisioning infrastructure on cloud platforms.

Install Terraform
Verify installation with:
terraform --version
4. AWS CLI (Optional, for AWS infrastructure)
If using AWS as the provider for Terraform, the AWS CLI should be configured.

Install AWS CLI
Configure AWS CLI with:
aws configure
5. Python (for Python automation scripts)
If using Python automation scripts, make sure Python 3 is installed.

Install Python
Verify installation with:
python3 --version
6. Docker Compose
Docker Compose is used to manage multi-container Docker applications.

Install Docker Compose
Verify installation with:
docker-compose --version
Setup Instructions

Clone the repository:
Clone the repository to your local machine:

git clone https://github.com/mariarodr1136/DevOpsAutomator.git
cd DevOpsAutomator
Build Docker images:
To build the Docker image, navigate to the Docker directory and use the docker-compose command:

docker-compose build
Configure Kubernetes:
Ensure that your Kubernetes cluster is up and running. You can use Minikube or a managed Kubernetes service like GKE or EKS.

For Minikube:

minikube start
kubectl config use-context minikube
Initialize Terraform:
If you're provisioning infrastructure on AWS or another cloud provider, navigate to the Terraform directory and initialize Terraform:

cd Terraform
terraform init
Run the Automation Script:
To deploy your application and provision the infrastructure, you can either use the Python or Bash script.

Using Python:
python3 Scripts/deploy_pipeline.py
Using Bash:
bash Scripts/provision_infrastructure.sh
Access Your Application:
Once the deployment is complete, you can access your application depending on how the Kubernetes services are configured:

If you're using a LoadBalancer type service, check the external IP with:
kubectl get services
If you're using Minikube, you can access the application through the Minikube service URL:
minikube service myapp-service --url

## Notes

- The Terraform script currently provisions an EC2 instance in AWS. Modify the main.tf file for additional infrastructure setups (e.g., VPC, S3, etc.).
- The Kubernetes configurations are set for a basic app deployment, but you can modify the deployment.yaml to include environment variables, secrets, or additional configurations like autoscaling.
- Docker Compose is set to run the containerized app on localhost:5000. Modify the ports in the docker-compose.yml file if needed.

## Troubleshooting

- Docker errors: If you encounter issues with Docker, ensure that Docker is running and properly configured. 
- Check Docker logs for more details:

docker logs <container_id>

- Kubernetes errors: Check the status of Kubernetes pods and services with:
kubectl get pods
kubectl get services

- Terraform errors: Terraform errors can often be related to missing provider credentials or syntax issues in the .tf files. Ensure your credentials are configured correctly and try re-running the Terraform commands.

## Contributing

Feel free to fork the project and submit pull requests if you have suggestions for improvements or additional features.