import tornado.web
import sispm

class Device:
    def __init__( self,
                  deviceName,
                  deviceSerialNumber,
                  deviceNumber,
                  deviceDescription ):
        self.name = deviceName
        self.serialNumber = deviceSerialNumber
        self.number = deviceNumber
        self.description = deviceDescription
        self.outlets = []

class DeviceHandler( tornado.web.RequestHandler ):
    def get( self ):
        devices = sispm.SisPM.listOfDevices
        self.write( "<h1>Devices</h1>" )
        self.write( "<ul>")
        for device in devices:
            self.write( '<li><a href="">%s</a></li>' % ( device ) )
        self.write( "</ul>" )
