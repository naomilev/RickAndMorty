# Rick and Morty Character API

This project provides a REST API to fetch information about Rick and Morty characters who are human, alive, and originate from Earth.

## Project Structure

- `kubernetes/`: Contains Kubernetes manifest files
- `helm/`: Contains the Helm chart for the application
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

# Rick and Morty API Helm Deployment

This section provides instructions for deploying the Rick and Morty API to Kubernetes using Helm.

## Prerequisites

- Kubernetes cluster (e.g., Minikube, GKE, EKS, etc.)
- Helm 3.x

## Deployment Steps

1. Navigate to the `helm` directory:
      `cd helm`

2. Install the Helm chart:
      `helm install rick-and-morty-api ./rick-and-morty-api`

   This command deploys the Rick and Morty API Helm chart to your Kubernetes cluster.

3. Check the installation status:
      `helm list`

   Look for the `rick-and-morty-api` release in the output.

4. Get the application URL:
   - If using Minikube:
         `minikube service rick-and-morty-api --url`

   - If using a cloud provider or external cluster:
     Get the external IP of the service:
         `kubectl get services`

     Look for the `rick-and-morty-api` service and note its external IP.

5. Access the API endpoints:
   - Characters: `<URL or IP>/api/characters`
   - Health Check: `<URL or IP>/api/healthcheck`

   Replace `<URL or IP>` with the URL or IP obtained in step 4.

### Customizing the Deployment

You can customize the deployment by modifying the values in the `helm/rick-and-morty-api/values.yaml` file. For example, you can change the number of replicas, update the image tag, or modify the resource limits.

After making changes, upgrade the release:
   `helm upgrade rick-and-morty-api ./rick-and-morty-api`

### Uninstalling the Chart

To uninstall the Helm chart:
   `helm uninstall rick-and-morty-api`

This command removes the Rick and Morty API deployment from your Kubernetes cluster.

## Troubleshooting

If you encounter issues deploying or accessing the API:

1. Check the status of the Helm release:
      `helm status rick-and-morty-api`

2. Ensure all pods are running:
      `kubectl get pods`

3. Check the logs of the API pods:
      `kubectl logs <pod-name>`

   Replace `<pod-name>` with the actual name of your API pod.

If problems persist, please consult the Helm and Kubernetes documentation for further troubleshooting steps.
