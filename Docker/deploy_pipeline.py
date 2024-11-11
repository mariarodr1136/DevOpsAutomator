import subprocess
import sys

def run_shell_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as err:
        print(f"Error: {err}")
        sys.exit(1)

if __name__ == "__main__":
    # Create the Docker registry secret
    run_shell_command("kubectl create secret docker-registry docker-registry-secret "
                      "--docker-server=https://index.docker.io/v1/ "
                      "--docker-username=mariarodr1136 "
                      "--docker-password=Angiechu1! "
                      "--docker-email=mrodr.contact@gmail.com")

    run_shell_command("docker-compose up -d")
    print("Docker containers are up.")

    run_shell_command("kubectl apply -f Kubernetes/")
    print("Kubernetes deployments are applied.")

    run_shell_command("terraform apply -auto-approve")
    print("Terraform infrastructure is provisioned.")