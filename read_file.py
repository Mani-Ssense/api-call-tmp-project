def read_file():
    with open('Dockerfile') as f:
        r = f.read()
        return r
