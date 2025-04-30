# C2_treatment_autonomy_valuator

The C2 treatment autonomy valuator check that the treatments to be applied over
a patient follows the autonomy value.

## Summary

 - Type: C2
 - Name: Treatment autonomy valuator
 - Version: 1.0.1 (April 30, 2025)
 - API: [1.0.1 (April 30, 2025)](https://raw.githubusercontent.com/VALAWAI/C2_treatment_autonomy_valuator/ASYNCAPI_1.0.1/asyncapi.yml)
 - VALAWAI API: [1.2.0 (March 9, 2024)](https://raw.githubusercontent.com/valawai/MOV/ASYNCAPI_1.2.0/asyncapi.yml)
 - Developed By: [IIIA-CSIC](https://www.iiia.csic.es)
 - License: [GPL 3](LICENSE)


## Generate Docker image

The recommended way to create a Docker image for this component is to run the script:
 
 ```
./buildDockerImages.sh
```

This script will build the image and tag it with the component's version 
(e.g., `valawai/c2_treatment_autonomy_valuator:1.0.1`).

The script offers several options for customization:

* **Build without cache:** Use `-nc` or `--no-cache` to skip using the cached
 image layers during the build process.
* **Specify tag:** Use `-t <tag>` or `--tag <tag>` to assign a custom tag name 
to the image (e.g., `./buildDockerImages.sh -t my-custom-image-name`).
* **Target architectures:** Use `-p <platforms>` or `--platform <platforms>` to specify
 the architectures (CPU types) for which the image should be built 
 (e.g., `./buildDockerImages.sh -p linux/arm64`). By default, the script builds 
 for `linux/arm64` and `linux/amd64` (both ARM and AMD processors).
* **Use default platforms:** Use `-dp` or `--default-platforms` to explicitly instruct
 the script to use the default architectures (linux/arm64 and linux/amd64).
* **Help message:** Use `-h` or `--help` to display a detailed explanation 
of all available options.

For example, to build an image with the tag `latest`, run:

```bash
./buildDockerImages.sh -t latest
```

This will create the container named `valawai/c2_treatment_autonomy_valuator:latest`.


### Docker environment variables

The following environment variables configure the Docker image's behavior, categorized by function:

#### I. RabbitMQ Connection Parameters:

These variables govern the connection to the RabbitMQ message broker.

*   `RABBITMQ_HOST`: Specifies the hostname or IP address of the RabbitMQ server. 
The default value is `mov-mq`.
*   `RABBITMQ_PORT`: Defines the port number used for communication with RabbitMQ. 
The default value is `5672`.
*   `RABBITMQ_USERNAME`: Sets the username for authenticating with the RabbitMQ server.
 The default value is `mov`.
*   `RABBITMQ_PASSWORD`: Sets the password for authenticating with the RabbitMQ server.
 The default value is `password`. *Note: For production environments, it is strongly advised 
 to avoid storing passwords directly in environment variables. Consider using secrets 
 management solutions.*
*   `RABBITMQ_MAX_RETRIES`: Determines the maximum number of attempts to establish a connection 
to RabbitMQ. The default value is `100`.
*   `RABBITMQ_RETRY_SLEEP`: Specifies the delay, in seconds, between connection attempts 
to RabbitMQ. The default value is `3`.

#### II. Logging Configuration:

These variables control the logging behavior of the application.

*   `LOG_CONSOLE_LEVEL`: Sets the minimum log level for messages displayed on the console. 
Possible values, in increasing order of severity, are `DEBUG`, `INFO`, `WARNING`, `ERROR`, `FATAL`,
 and `CRITICAL`. The default value is `INFO`.
*   `LOG_FILE_LEVEL`: Sets the minimum log level for messages written to the log file. Possible 
values are the same as `LOG_CONSOLE_LEVEL`. The default value is `DEBUG`.
*   `LOG_FILE_MAX_BYTES`: Defines the maximum size, in bytes, of the log file before it is rolled
 over (renamed and a new file created). The default value is `1000000`.
*   `LOG_FILE_BACKUP_COUNT`: Specifies the number of rolled-over log files to retain. Older files 
are deleted when this limit is exceeded. The default value is `5`.
*   `LOG_DIR`: Specifies the directory where log files are stored. The default value is `logs`.
*   `LOG_FILE_NAME`: Defines the base filename for the log file within the `LOG_DIR`. The default 
value is `c2_treatment_autonomy_valuator.txt`.

#### III. Component Identification:*

This variable manages the storage of the component's unique identifier.

*   `COMPONET_ID_FILE_NAME`: Defines the filename (within the `LOG_DIR`) where the component's 
identifier, obtained during registration with the MOV, is stored. The default value is
 `component_id.json`.

#### IV. Autonomy Value Calculation Weights:

These variables define the relative importance of various factors in the calculation
of the autonomy value. Each variable represents a weighting factor applied to the 
corresponding attribute.

*  `IS_COMPETENT_WEIGHT`: Weight applied to the patient's competency status (i.e., their 
legal capacity to make decisions). Default value: `0.25`.
*  `HAS_BEEN_INFORMED_WEIGHT`: Weight applied to whether the patient has been adequately 
informed about their condition and treatment options. Default value: `0.5`.
*  `IS_COERCED_WEIGHT`: Weight applied to whether the patient is being coerced into making
 decisions. Default value: `0.25`.

 
### Docker health check

The component stores its registration details in a file. Unless overridden by the **COMPONET_ID_FILE_NAME**
environment variable, this file is located at **/app/${LOG_DIR:-logs}/${COMPONET_ID_FILE_NAME:-component_id.json}**.
This file is deleted when the component is unregistered. Therefore, checking the file's existence and size
provides a straightforward health check. The following Docker Compose snippet illustrates a health check
configuration:

```
    healthcheck:
      test: ["CMD-SHELL", "test -s /app/logs/component_id.json"]
      interval: 1m
      timeout: 10s
      retries: 5
      start_period: 1m
      start_interval: 5s
```


## Deploying the Component

This section shows you how to get the C2 Treatment Autonomy Valuator up 
and running using Docker Compose.

### What you'll need:

*   **Docker:** This is a tool that lets you run software in isolated "containers."
 You can download it from [https://www.docker.com/get-started](https://www.docker.com/get-started).
*   **Docker Compose:** This tool helps you manage multiple Docker containers
 at once. It's usually included with Docker Desktop, or you can install it separately. 
 See the Docker documentation for instructions.

## Deployment on a VALAWAI Environment

The `docker-compose.yml` file defines how to deploy the C2 Treatment Autonomy Valuator component within
a VALAWAI environment.  It includes profiles for the Master of VALAWAI (MOV) and a mocked email server.

To start the component with MOV and the mail server, use the following command:

```bash
COMPOSE_PROFILES=mov docker compose up -d
```

The MOV user interface is available at [http://localhost:8081](http://localhost:8081), 
and the RabbitMQ management interface at [http://localhost:8082](http://localhost:8082) 
with credentials `mov:password`.

### Configuration 

Environment variables can be configured by creating a `.env` file (see 
[Docker Compose documentation](https://docs.docker.com/compose/environment-variables/env-file/)).  
Define variables in the `.env` file using the format `VARIABLE_NAME=value`.  For example:

```
MQ_HOST=rabbitmq.valawai.eu
MQ_USERNAME=c0_patient_treatment_ui
MQ_PASSWORD=lkjagb_ro82t¿134
```

The following environment variables are supported:

* **`C2_TREATMENT_AUTONOMY_VALUATOR_TAG`:** Tag for the C2 NIT Protocol Manager Docker image. Default: `latest`
* **`MQ_HOST`:** Hostname of the message queue broker. Default: `mq`
* **`MQ_PORT`:** Port of the message queue broker. Default: `5672`
* **`MQ_UI_PORT`:** Port of the message queue broker UI. Default: `8081`
* **`MQ_USER`:** Username for accessing the message queue broker. Default: `mov`
* **`MQ_PASSWORD`:** Password for accessing the message queue broker. Default: `password`
* **`RABBITMQ_TAG`:** Tag for the RabbitMQ Docker image. Default: `management`
* **`MONGODB_TAG`:** Tag for the MongoDB Docker image. Default: `latest`
* **`MONGO_PORT`:** Port where MongoDB is accessible. Default: `27017`
* **`MONGO_ROOT_USER`:** Root username for MongoDB. Default: `root`
* **`MONGO_ROOT_PASSWORD`:** Root password for MongoDB. Default: `password`
* **`MONGO_LOCAL_DATA`:** Local directory for MongoDB data. Default: `~/.mongo_data/patienttreatmentuiMovDB`
* **`MOV_DB_NAME`:** Name of the database used by MOV. Default: `movDB`
* **`MOV_DB_USER_NAME`:** Username used by MOV to access the database. Default: `mov`
* **`MOV_DB_USER_PASSWORD`:** Password used by MOV to access the database. Default: `password`
* **`MOV_TAG`:** Tag for the MOV Docker image. Default: `latest`
* **`MOV_UI_PORT`:** Port where the MOV UI is accessible. Default: `8081`


If you want to change some settings, you can create a file named `.env` 
in the same folder as the `docker-compose.yml` file. Here's how it works:

1.  Create a new file named `.env` in your text editor.
2.  Add lines like this to change settings:

 ```
 MQ_HOST=my.custom.rabbitmq.server
 MQ_PASSWORD=my_secret_password
 ```

 This example changes the message queue server and the password.

Here's a list of the settings you can change in the `.env` file:

*   `` (usually leave this as `latest`)
*   `MQ_HOST` (the address of the message queue)
*   `MQ_PORT` (the port of the message queue, usually 5672)
*   `MQ_UI_PORT` (the port of the message queue web interface, usually 8081)
*   `MQ_USER` (the username for the message queue)
*   `MQ_PASSWORD` (the password for the message queue - **Important:** Change this for real use!)
*   `RABBITMQ_TAG` (usually leave this as `management`)
*   `MONGODB_TAG` (usually leave this as `latest`)
*   `MONGO_PORT` (the port for the database, usually 27017)
*   `MONGO_ROOT_USER` (the database root username)
*   `MONGO_ROOT_PASSWORD` (the database root password - **Important:** Change this for real use!)
*   `MONGO_LOCAL_DATA` (where the database files are stored on your computer)
*   `MOV_DB_NAME` (the name of the database MOV uses)
*   `MOV_DB_USER_NAME` (the username MOV uses to access the database)
*   `MOV_DB_USER_PASSWORD` (the password MOV uses to access the database - **Important:** Change this for real use!)
*   `MOV_TAG` (usually leave this as `latest`)
*   `MOV_UI_PORT` (the port for the MOV web interface, usually 8080)
*   `LOG_LEVEL` (how much logging information you see; usually `INFO`)

### Database Considerations

The database is created only during the initial deployment. If you modify 
any database parameters, you must recreate the database. To do this, remove 
the directory specified by the `MONGO_LOCAL_DATA` environment variable and 
restart the Docker Compose deployment.

### Stopping the Deployment

To stop all started containers, use the following command:

```bash
COMPOSE_PROFILES=mov docker-compose down
```
  
## Development Environment

This guide explains how to set up a development environment for the C2 Treatment
Autonomy Valuator.

### Prerequisites

* Docker and Docker Compose must be installed on your system.

### Setting Up the Environment

1. **Start the Development Environment:** Open your terminal and run the following
script:

```bash
./startDevelopmentEnvironment.sh
```
This script launches a Bash shell configured for development. All subsequent commands should be run within this development shell.

2. **Available Commands (within the development shell):**

* **run:** Starts the C2 Treatment Autonomy Valuator component.
* **testAll:** Runs all unit tests.
* **test test/test_something.py:** Runs unit tests defined in `test_something.py`.
* **test test/test_something.py::TestClassName::test_do_something:**
Runs the specific unit test `test_do_something` within the class `TestClassName` in `test_something.py`.
* **coverage:** Runs all unit tests and generates a coverage report.
* **fmt:** Runs a static code analyzer to check for formatting and style issues.

### Development Environment Components

The `startDevelopmentEnvironment.sh` script launches the following services:

* **RabbitMQ:** A message broker facilitating communication between components. Access 
the management interface at [http://localhost:8081](http://localhost:8081) using the 
credentials `mov:password`.

* **MongoDB:** A NoSQL database used by the MOV. The database name is `movDB`, and 
the default credentials are `mov:password`.

* **Mongo Express:** A web interface for managing the MongoDB database. Access it at 
[http://localhost:8082](http://localhost:8082) using credentials `mov:password`.

* **Master of VALAWAI (MOV):** Manages network topology and component connections. If running,
 access the MOV UI at [http://localhost:8084](http://localhost:8084).

This development environment provides a pre-configured infrastructure for developing, testing, 
and debugging the C2 Treatment Autonomy Valuator component, streamlining the development process 
and enabling efficient iteration.


## Links

 - [C2 Treatment autonomy valuator documentation](https://valawai.github.io/docs/components/C2/treatment_autonomy_valuator)
 - [Master Of VALAWAI tutorial](https://valawai.github.io/docs/architecture/implementations/mov)
 - [VALWAI documentation](https://valawai.github.io/docs/)
 - [VALAWAI project web site](https://valawai.eu/)
 - [Twitter](https://twitter.com/ValawaiEU)
 - [GitHub](https://github.com/VALAWAI)
 