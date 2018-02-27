import json, logging, sys, time, zmq

# logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.info("Starting TCP server ...")


# server - the processing server

context = zmq.Context()
socket = context.socket(zmq.REP)
url = "tcp://127.0.0.1:5555"
socket.bind(url)
logging.info(f"TCP server running at: {url}")


while True:
    # check for messages from client
    msg = socket.recv()

    pong = json.loads(msg.decode())
    delta = time.time() - pong["now"]

    pong["delta"] = delta
    serialised_pong = json.dumps(pong)

    socket.send_string(serialised_pong)
    
