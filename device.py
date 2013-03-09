import tornado.web
import sispm

class DeviceHandler( tornado.web.RequestHandler ):
    def get( self ):
        devices = sispm.SisPM.listOfDevices
        deviceSerialNumber = None
        try:
            # try to fetch the neccessary argument
            deviceSerialNumber = self.get_argument( 'serialNumber' )
        except tornado.web.HTTPError:
            # if the argument is not given, show default device overview page
            self.write( "<h1>Devices</h1>" )
            self.write( "<ul>")
            for deviceSerialNumber in devices:
                device = devices[ deviceSerialNumber ]
                self.write( '<li><a href="device?serialNumber=%s">%s</a></li>'
                            % ( deviceSerialNumber,
                                device[ 'name' ] ) )
                self.write( "</ul>" )
            self.flush()
            return
        # otherwise show the device details
        device = devices[ deviceSerialNumber ]
        self.write( '<h1>Outlets for %s</h1>' % ( device[ 'name' ] ) )
        self.write( '<p>%s</p>' % ( device[ 'description' ] ) )
        statusOfOutlets = sispm.SisPM.statusOfOutlets( deviceSerialNumber )
