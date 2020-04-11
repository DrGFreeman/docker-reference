from pathlib import Path

if __name__ == "__main__":

    p = Path("/data")
    files = p.glob("*")

    for file in files:
        print(file.as_posix())
