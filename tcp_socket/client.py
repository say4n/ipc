import json, time, zmq

# client - the agent which will work

context = zmq.Context()
socket = context.socket(zmq.REQ)
url = "tcp://127.0.0.1:5555"
socket.connect(url)

ping = {"now": time.time()}
serialised_ping = json.dumps(ping)
socket.send_string(serialised_ping)

# Get result from server (not necessary)
msg = socket.recv()
pong = json.loads(msg.decode())

print(f"IPC delay {pong['delta']} sec")
