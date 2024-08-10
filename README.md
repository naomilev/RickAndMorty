# Rick and Morty Character API

This project provides a REST API to fetch information about Rick and Morty characters who are human, alive, and originate from Earth.

## Project Structure

- `kubernetes/`: Contains Kubernetes manifest files
- `src/`: Contains the application source code (`app.py`)
- `Dockerfile`: Defines the container image for the application
- `requirements.txt`: Lists the Python dependencies

## Building and Running the Docker Image

1. Build the Docker image:
      `docker build -t rick-and-morty-api`

2. Run the Docker container:
      `docker run -p 8080:8080 rick-and-morty-api`

The application will now be running and accessible at `http://localhost:8080`.

## REST API Endpoints

1. Healthcheck
- URL: `/healthcheck`
- Method: GET
- Description: Check if the application is running correctly

2. Get Characters
- URL: `/characters`
- Method: GET
- Description: Fetch all human characters from Earth who are alive

## Fetching Data

You can use any HTTP client to fetch data from these endpoints. Here are examples using curl:

1. Do Healthcheck:
      `curl http://localhost:8080/healthcheck`
   
2. Get Characters:
      `curl http://localhost:8080/characters`

Note: Make sure the Docker container is running before trying to access these endpoints.

# Rick and Morty API Kubernetes Deployment

This README provides instructions for deploying the Rick and Morty API to Kubernetes using Minikube.

## Prerequisites

- Minikube
- kubectl
- Docker (for building and pushing images)

## Deployment Instructions

Choose the instructions based on your operating system:

- [MacOS Instructions](#macos-instructions)
- [Linux/Windows Instructions](#linuxwindows-instructions)

## MacOS Instructions

### Prerequisites
- Minikube
- kubectl
- Docker

### Deployment Steps

1. Start Minikube:
      `minikube start`
   
2. Apply the Kubernetes manifests:
    `kubectl apply -f kubernetes/Deployment.yaml`
    `kubectl apply -f kubernetes/Service.yaml`
    `kubectl apply -f kubernetes/Ingress.yaml`
   
3. Enable the Ingress addon in Minikube:
    `minikube addons enable ingress`
   
4. Get the URL to access your service:
    `minikube service ingress-nginx-controller -n ingress-nginx --url`
   
5. Access the API endpoints:
   - Characters: `<URL from step 4>/characters`
   - Health Check: `<URL from step 4>/healthcheck`

   For example:
      `curl http://127.0.0.1:port/characters`
      `curl http://127.0.0.1:port/healthcheck`
   Replace `port` with the port obtained in step 4.

### Cleaning Up

To remove the deployed resources:
   `kubectl delete -f kubernetes/Ingress.yaml`
   `kubectl delete -f kubernetes/Service.yaml`
   `kubectl delete -f kubernetes/Deployment.yaml`

## Linux/Windows Instructions

### Prerequisites
- Minikube
- kubectl
- Docker

### Deployment Steps

1. Start Minikube:
    minikube start

2. Apply the Kubernetes manifests:
    kubectl apply -f kubernetes/Deployment.yaml
    kubectl apply -f kubernetes/Service.yaml
    kubectl apply -f kubernetes/Ingress.yaml

4. Enable the Ingress addon in Minikube:
    minikube addons enable ingress

5. Get the Minikube IP:
    minikube ip

6. Access the API endpoints:
    - Characters: `http://minikube-ip/characters`
    - Health Check: `http://minikube-ip/healthcheck`

   For example:
    curl http://minikube-ip/characters
    curl http://minikube-ip/healthcheck
   Replace `minikube-ip` with the IP address obtained in step 4.

### Cleaning Up

To remove the deployed resources:
      kubectl delete -f kubernetes/Ingress.yaml
      kubectl delete -f kubernetes/Service.yaml
      kubectl delete -f kubernetes/Deployment.yaml

## Troubleshooting

If you encounter issues accessing the API:

1. Ensure all pods are running:
    kubectl get pods

2. Check the Ingress controller status:
    kubectl get pods -n ingress-nginx

4. Verify the Ingress resource:
    kubectl get ingress
    kubectl describe ingress rick-and-morty-api-ingress

5. Check the logs of the API pods:
    kubectl logs `<pod-name>`
   Replace `<pod-name>` with the actual name of your API pod.
   
   If problems persist, please check the Minikube and Kubernetes documentation for your specific environment.

## Note on Cross-Platform Compatibility

These instructions have been primarily tested on macOS. While they should work on Linux and Windows, there might be slight variations depending on your specific setup. If you encounter any issues on Linux or Windows, please:

1. Ensure Minikube is correctly installed for your OS.
2. Check that your Minikube driver is compatible with your system.
3. For Windows users, you may need to use Windows Subsystem for Linux (WSL) for the best compatibility.

If you successfully run this on Linux or Windows, please consider contributing your experience back to this project to help other users.

For the most up-to-date information on platform-specific configurations, please refer to the official Minikube documentation:
[Minikube Start Guide](https://minikube.sigs.k8s.io/docs/start/)




















