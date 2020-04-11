# Mount host volume into Docker container

This application shows how to mount a folder of the host so it is accessible from within the container.

## Application

The `glob.py` application simply finds all the files in the `/data` folder of the container and prints the list of files, including their relative path.

```python
# glob.py
from pathlib import Path

if __name__ == "__main__":

    p = Path("/data")
    files = p.glob("*")

    for file in files:
        print(file.as_posix())
```

## Dockerfile

The `Dockerfile` simply copies the `glob.py` application and runs it.

```
FROM python:3

COPY glob.py ./

CMD [ "python", "glob.py" ]
```

## Usage

### Build

```
$ docker build -t glob .
```

### Run

Use the `-v` option to mount the host path to `/data` in the container.

```
$ docker run -rm -v absolute_host_path:/data glob
```

This will print out the content of `absolute_host_path`.

## References

1. https://docs.docker.com/storage/volumes/.