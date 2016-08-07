# coding: UTF-8
import time
import tornado
import tornado.ioloop
import tornado.iostream
import json
import zmq
from config import zmqconfig
from zmq.eventloop import ioloop, zmqstream
context = zmq.Context()
ioloop.install()

class service:

    def __init__(self):
        self.ioloop = ioloop.IOLoop().current(True)
        return


    def process_message_one(self, msg):
        print "get thread one message"
        print "processing .....", msg
        return

    def process_message_two(self, msg):
        print "get thread two message"
        print "processing .....", msg
        return

    def timeout(self):
        print "thread three timeout"
        print "thread two timeout"
        data = {}
        data['thread'] = 'three'
        self.socket_to_others.send(zmqconfig.three_to_one_subject, zmq.SNDMORE)
        self.socket_to_others.send(json.dumps(data))
        self.socket_to_others.send(zmqconfig.three_to_two_subject, zmq.SNDMORE)
        self.socket_to_others.send(json.dumps(data))
        self.ioloop.add_timeout(time.time() + 3, self.timeout)
        return

    def run(self):
        self.socket_to_others = zmqconfig.context.socket(zmq.PUB)
        self.socket_to_others.bind(zmqconfig.three_zmq_addr)
        self.socket_from_two = zmqconfig.context.socket(zmq.SUB)
        self.socket_from_two.connect(zmqconfig.two_zmq_addr)
        self.socket_from_two.setsockopt(zmq.SUBSCRIBE, zmqconfig.two_to_three_subject)
        self.stream_from_two_sub = zmqstream.ZMQStream(self.socket_from_two)
        self.stream_from_two_sub.on_recv(self.process_message_two)
        self.socket_from_one = zmqconfig.context.socket(zmq.SUB)
        self.socket_from_one.connect(zmqconfig.one_zmq_addr)
        self.socket_from_one.setsockopt(zmq.SUBSCRIBE, zmqconfig.one_to_three_subject)
        self.stream_from_one_sub = zmqstream.ZMQStream(self.socket_from_one)
        self.stream_from_one_sub.on_recv(self.process_message_one)
        self.ioloop.add_timeout(time.time(), self.timeout)
        self.ioloop.start()
        return
