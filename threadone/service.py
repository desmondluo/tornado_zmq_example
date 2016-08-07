# coding: UTF-8
import time
import tornado
import tornado.ioloop
import tornado.iostream
import tornado.web
import json
import zmq
from urls import urls
from config import zmqconfig
from zmq.eventloop import ioloop, zmqstream
from zmq.eventloop.ioloop import IOLoop
from zmq.eventloop.ioloop import ZMQIOLoop
#ioloop.install()
#application = tornado.web.Application(urls)
class service:

    def __init__(self):
        self.ioloop = ZMQIOLoop()
        self.ioloop.install()
        return

    def process_message_two(self, msg):
        print "get thread two message"
        print "processing .....", msg
        return

    def process_message_three(self, msg):
        print "get thread three message"
        print "processing......", msg
        return

    def timeout(self):
        print "thread one timeout"
        data = {}
        data['thread'] = 'one'
        self.socket_to_others.send(zmqconfig.one_to_two_subject, zmq.SNDMORE)
        self.socket_to_others.send(json.dumps(data))
        self.socket_to_others.send(zmqconfig.one_to_three_subject, zmq.SNDMORE)
        self.socket_to_others.send(json.dumps(data))
        self.ioloop.add_timeout(time.time() + 3, self.timeout)
        return

    def run(self):
        self.socket_to_others = zmqconfig.context.socket(zmq.PUB)
        self.socket_to_others.bind(zmqconfig.one_zmq_addr)
        self.socket_from_two = zmqconfig.context.socket(zmq.SUB)
        self.socket_from_two.connect(zmqconfig.two_zmq_addr)
        self.socket_from_two.setsockopt(zmq.SUBSCRIBE, zmqconfig.two_to_one_subject)
        self.stream_from_two_sub = zmqstream.ZMQStream(self.socket_from_two)
        self.stream_from_two_sub.on_recv(self.process_message_two)
        self.socket_from_three = zmqconfig.context.socket(zmq.SUB)
        self.socket_from_three.connect(zmqconfig.three_zmq_addr)
        self.socket_from_three.setsockopt(zmq.SUBSCRIBE, zmqconfig.three_to_one_subject)
        self.socket_from_three_sub = zmqstream.ZMQStream(self.socket_from_three)
        self.socket_from_three_sub.on_recv(self.process_message_three)
        self.ioloop.add_timeout(time.time(), self.timeout)
        application = tornado.web.Application(urls)
        application.listen(8887)
        self.ioloop.start()
        return
