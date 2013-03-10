#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import sispm
import device
import outlet

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write( "<h1>SisPM Web</h1>" )
        self.write( '<a href="device">Devices</a>' )

application = tornado.web.Application([
    ( r"/", MainHandler ),
    ( r"/device/?", device.DevicesHandler ),
    ( r"/device/([0-9A-Za-z:]+)/?", device.DeviceHandler ),
    ( r"/device/([0-9A-Za-z:]+)/outlet/([0-9])+/?", outlet.OutletHandler ),
    ( r"/device/([0-9A-Za-z:]+)/outlet/([0-9])+/status/(True|False)", outlet.OutletStatusHandler )
])

if __name__ == "__main__":
    sispm.SisPM.initializeListOfDevices()
    print sispm.SisPM.listOfDevices
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
