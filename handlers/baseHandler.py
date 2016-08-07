#-*- coding: utf-8 -*-
import tornado.web
from appGlobal import appGlobal


class baseHandler(tornado.web.RequestHandler):
    code = 0
    message = ""
    def initialize(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        return

    def val(self, key):
        ret = None
        for k in self.request.query_arguments:
            if (k == key):
                ret = self.request.query_arguments[k]
                break
        if (ret != None and len(ret) == 1):
            ret = ret[0]
        if (ret is None):
            for k in self.request.body_arguments:
                if (k == key):
                    ret = self.request.body_arguments[k]
                    break
            if (ret != None and len(ret) == 1):
                ret = ret[0]
        return ret

    def dispalyByJson(self, data):
        sdata = {
            'code': self.code,
            'message': self.message,
            'response': data
        }
        self.write(sdata)

    def setError(self, code, message):
        self.code = code
        self.message = message