import threading
import time
import random
import logging

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None, queue=None):
        super().__init__()

        self.target = target
        self.name = name
        self.queue = queue

    def run(self, queue=None):
        while True:
            if not self.queue.full():
                item = random.randint(1,10)
                self.queue.put(item)
                logging.debug('Putting ' + str(item)  
                              + ' : ' + str(self.queue.qsize()) + ' items in queue')