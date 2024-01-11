# Sample Pytest API Test with Using Swagger

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

After running, to generate the cucumber report (cucumber_report.html)
```bash
npm run report
```

It is not expected that you complete every task, however, please give your best effort 

You will be scored based on your ability to complete the following tasks:

- [ ] Install and setup this repository on your personal computer
- [ ] Complete the automation tasks listed below

### Tasks
- [ ] Modify the scenario 'Validate the login page title' from [login.feature](features/login.feature#8) which runs but fails. Determine the cause of the failure and update the scenario to pass in the test
- [ ] Extend the scenario 'Validate login error message' from [login.feature](features/login.feature#10) which runs and passes but is missing a step. Extend the scenario to validate the error message received.
- [ ] Modify and extend the 'Validate successful purchase text' from [purchase.feature](features/purchase.feature#6) with steps for each comment listed. Consider writing a new steps.ts file along with an appropriate page.ts
- [ ] Extend the testing coverage with anything you believe would be beneficial