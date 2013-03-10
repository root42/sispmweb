#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import device
import sispm

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write( "<h1>SisPM Web</h1>" )
        self.write( '<a href="device">Devices</a>' )

application = tornado.web.Application([
    ( r"/", MainHandler ),
    ( r"/device", device.DevicesHandler ),
    ( r"/device/([0-9A-Za-z:]+)", device.DeviceHandler ),
])

if __name__ == "__main__":
    sispm.SisPM.initializeListOfDevices()
    print sispm.SisPM.listOfDevices
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
