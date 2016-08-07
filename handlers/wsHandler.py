#-*- coding: utf-8 -*-

import tornado.websocket
import uuid
import json
import hashlib
import time

class wsHandler(tornado.websocket.WebSocketHandler):
    __isAuth = False
    __username = ""
    def check_origin(self, origin):
        return True

    def Authed(self):
        return self.__isAuth

    def getid(self):
        return self.id

    def open(self):
        self.id = uuid.uuid4()
        print 'new Connection'
        self.write_message("{}")

    def on_message(self, message):
        print "test"

