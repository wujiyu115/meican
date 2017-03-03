# -*- coding: utf-8 -*-
# @Author: wujiyu
# @Date:   2017-02-27 13:22:32
# @Last Modified by:   wujiyu
# @Last Modified time: 2017-02-27 19:06:55
import threading

class Message(object):
    """docstring for Message"""
    _instance_lock = threading.Lock()

    @staticmethod
    def instance():
        if not hasattr(Message, "_instance"):
            with Message._instance_lock:
                if not hasattr(Message, "_instance"):
                    Message._instance = Message()
        return Message._instance

    def __init__(self):
        super(Message, self).__init__()
        self._handlers = {}

    def sub(self, topic, handler):
        handlers = self._handlers.get(topic)
        if handlers == None:
            self._handlers[topic] = [handler]
            return
        for v in handlers:
            if v == handler:
                return
        handlers.append(handler)
        pass

    def unsub(self, topic, handler):
        assert(handler)
        handlers = self._handlers.get(topic)
        assert(handlers)
        for v in handlers:
            if v == handler:
                table.remove(handlers, i)
        pass

    def pub(self, topic, *args):
        handlers = self._handlers.get(topic)
        if handlers == None:
            return
        for handler in handlers:
            handler(*args)
        pass

    def publish(self, evt_id, *args):
        self.pub(evt_id, *args)

    def subscribe(self, evt_id, handler):
        self.sub(evt_id, handler)

    def unsubscribe(self, evt_id, handler):
        self.unsub(evt_id, handler)
