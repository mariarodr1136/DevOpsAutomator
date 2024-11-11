# Dockerfile
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Make the script directory
RUN mkdir -p /app/Scripts

# Copy the deployment script
COPY deploy_pipeline.py /app/Scripts/

# Define the command to run your app
CMD ["python", "Scripts/deploy_pipeline.py"]