import tornado
import tornado.ioloop
import tornado.web
import threading
import time
import multiprocessing
from threadone import service as oneservice
from threadtwo import service as twoservice
from threadthree import service as threeservice
from zmq.eventloop import ioloop, zmqstream
#ioloop.install()
import zmq
context = zmq.Context()

def timeout():
    print "timeout"
    return

def onethread():
    one = oneservice.service()
    one.run()
    return

def twothread():
    two = twoservice.service()
    two.run()
    return

def threethread():
    three = threeservice.service()
    three.run()
    return


if __name__ == "__main__":
   # threadone = threading.Thread(target=onethread, args=())
   # threadone.start()
    threadone = multiprocessing.Process(target=onethread, args=())
    threadtwo = multiprocessing.Process(target=twothread, args=())
    threadthree = multiprocessing.Process(target=threethread, args=())
    threadthree.start()
    threadtwo.start()

    threadone.start()
   # tornado.ioloop.IOLoop().instance().start()


    #threadone.join()
  #  ioloop.IOLoop().instance().start()
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    # ioloop.IOLoop().instance().start()
    # threadone.join()
    # threadtwo.join()
    # threadthree.join()