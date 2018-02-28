import json, os, tempfile


pipename = "ipc_pipe"
tmpdir = tempfile.mkdtemp()
filename = os.path.join(tmpdir, pipename)

with open("config.cfg", "w") as config:
    config.write(filename)

try:
    os.mkfifo(filename)
except Exception:
    print("Exception")
    os.remove(filename)
    os.mkfifo(filename)


pipe_out = os.open(filename, os.O_NONBLOCK | os.O_WRONLY)

for i in range(1000):
    data = json.dumps({"num": i}).encode('utf-8')
    os.write(pipe_out, data) 

os.close(pipe_out)