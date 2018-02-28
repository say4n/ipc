import json, os, tempfile

filename = open("config.cfg", "r").readline()

with os.open(filename, os.O_NONBLOCK | os.O_RDONLY) as pipe_in:
    while True:
        line = pipe_in.readline()

        if line is None:
            exit(-1)

        line = line.decode('utf-8')
        print(json.load(line))

os.remove(filename)
os.rmdir(tmpdir)
