import tornado
import tornado.ioloop
import tornado.web
import threading
import time
import os
import ctypes

class ThreadService:
    def timeout(self):
        print 'Thread ' + str(ctypes.CDLL('libc.so.6').syscall(186)) + ' TimeOut'
        self.ioloop.add_timeout(time.time() + 3, self.timeout)

    def run(self):
        print 'Thread ' + str(ctypes.CDLL('libc.so.6').syscall(186))
        tornado.ioloop.IOLoop.instance().make_current()
        self.ioloop = tornado.ioloop.IOLoop.current()
        self.ioloop.add_timeout(time.time(), self.timeout)
        #self.ioloop.start()

def onethread():
    one = ThreadService()
    one.run()
    return

def twothread():
    two = ThreadService()
    two.run()
    return


if __name__ == "__main__":
    print 'Main Thread ' + str(os.getpid())
    threadone = threading.Thread(target=onethread, args=())
    threadtwo = threading.Thread(target=twothread, args=())
    threadone.start()
    threadtwo.start()
    tornado.ioloop.IOLoop.instance().start()
    threadone.join()
    threadtwo.join()
    # ioloop.IOLoop().instance().start()
    # threadone.join()
    # threadtwo.join()
    # threadthree.join()