# Run a simple Dash app in a Docker container

This application shows how to run a simple Dash application in a docker container, including installation of dependencies and mapping of the container port to that of the host.

## Application

The Dash application is defined in the `app` folder. The application dependencies are defined in the `requirements.txt` file. The `serve.py` script is runs the application on port 5000 of the container. 

## Dockerfile

The `Dockerfile` sets the working directory in the container, then copies the `requirements.txt` file and installs the dependencies using `pip`. The application is then copied in the container and the `serve.py` script is launched.

```Dockerfile
FROM python:3.7.7-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./serve.py" ]

```

## Usage

### Build

```
$ docker build -t dash .
```

### Run

Use the `-p` option to map port 5000 of the container to port 8080 of the host.

```
$ docker run --rm -p 8080:5000 -d dash
```

Open a browser to http://localhost:8080 to use the application.

## References

1. https://docs.docker.com/config/containers/container-networking/
1. https://hub.docker.com/_/python/