import logging
import queue

from producer import ProducerThread
from consumer import ConsumerThread

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-8s) %(message)s')

BUF_SIZE = 100
q = queue.Queue(BUF_SIZE)

if __name__ == "__main__":
    pthread = ProducerThread(name="producer", queue=q)
    cthread = ConsumerThread(name="consumer", queue=q)

    pthread.start()
    cthread.start()
