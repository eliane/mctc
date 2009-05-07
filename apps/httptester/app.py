#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import rapidsms
from apps.httptester.models import Message
import datetime

class App(rapidsms.app.App):
    def handle(self, message):
        self.debug("got message %s" % (message))
        
    def outgoing(self, message):
        pass
