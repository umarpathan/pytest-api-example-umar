# Sample Pytest API Test Using Swagger

## System Requirements

python 3.x.x


## Setup

// Install Visual Studio Code (or any editor)

https://code.visualstudio.com/download


// Install Python 3.x.x (latest)

https://www.python.org/downloads/

// Install Docker Desktop (requires computer restart after installation). No need to sign up for an account. Ensure you've started the Docker application after restart.

https://docs.docker.com/get-docker/

// Pull and run the image from https://github.com/swagger-api/swagger-petstore
```bash
docker pull swaggerapi/petstore3:1.0.17
docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:1.0.17
```

// Once it is running, you can access the SwaggerUI in a browser via http://localhost:8080/

// You can stop the Docker container via command line (docker ps, then take the container id and do docker stop <container_id>) or using Docker Desktop under Containers -> swaggerapi-petstore3 then hit the Stop button

// Consider toggling the media type dropdown in the swagger documentation to application/json

// Create a project in vscode, open the terminal
```bash
git clone https://github.com/automationExamples/pytest-api-example.git
pip install requests pytest pyhamcrest jsonschema
```

### Recommended vscode extensions

Python, Pylance, autopep8


## Instructions
To run the test
```bash
pytest -v
```

It is not expected that you complete every task, however, please give your best effort 

You will be scored based on your ability to complete the following tasks:

- [ ] Install and setup this repository on your personal computer
- [ ] Complete the automation tasks listed below

### Tasks
- [ ] xxxx