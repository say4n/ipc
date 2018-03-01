import threading
import time
import random
import logging

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None, queue=None):
        super().__init__()
        
        self.target = target
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():
                item = self.queue.get()
                logging.debug('Getting ' + str(item) 
                              + ' : ' + str(self.queue.qsize()) + ' items in queue')
                time.sleep(random.random())