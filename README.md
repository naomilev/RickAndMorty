# Rick and Morty Character API

This project provides a REST API to fetch information about Rick and Morty characters who are human, alive, and originate from Earth.

## Building and Running the Docker Image

1. Build the Docker image:
   docker build -t rick-and-morty-api

2. Run the Docker container:
   docker run -p 8080:8080 rick-and-morty-api

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

1. Healthcheck:
   curl http://localhost:8080/healthcheck
   
2. Get Characters:
   curl http://localhost:8080/characters

Note: Make sure the Docker container is running before trying to access these endpoints.
