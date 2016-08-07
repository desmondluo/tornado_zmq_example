import tornado
import tornado.ioloop
import tornado.web
import time
import multiprocessing
from threadone import service as oneservice
from threadtwo import service as twoservice
from threadthree import service as threeservice
import zmq
context = zmq.Context()

def timeout():
    print "timeout"
    return

def one():
    one = oneservice.service()
    one.run()
    return

def two():
    two = twoservice.service()
    two.run()
    return

def three():
    three = threeservice.service()
    three.run()
    return


if __name__ == "__main__":
    serviceone = multiprocessing.Process(target=one, args=())
    servicetwo = multiprocessing.Process(target=two, args=())
    servicethree = multiprocessing.Process(target=three, args=())
    servicethree.start()
    servicetwo.start()
    serviceone.start()

    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    # ioloop.IOLoop().instance().start()
    # threadone.join()
    # threadtwo.join()
    # threadthree.join()