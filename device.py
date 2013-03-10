import tornado.web
import sispm

class DeviceHandler( tornado.web.RequestHandler ):
    def get( self, deviceSerialNumber ):
        devices = sispm.SisPM.listOfDevices
        device = devices[ deviceSerialNumber ]
        self.write( '<h1>Outlets for %s</h1>' % ( device[ 'name' ] ) )
        self.write( '<p>%s</p>' % ( device[ 'description' ] ) )
        statusOfOutlets = sispm.SisPM.statusOfOutlets( deviceSerialNumber )
        self.write( "<ul>")
        for outlet in statusOfOutlets:
            self.write( "<li>%s %s</li>" % ( outlet,
                                             str( statusOfOutlets[ outlet ] ) ) )
        self.write( "</ul>" )

class DevicesHandler( tornado.web.RequestHandler ):
    def get( self ):
        devices = sispm.SisPM.listOfDevices
        self.write( "<h1>Devices</h1>" )
        self.write( "<ul>")
        for deviceSerialNumber in devices:
            device = devices[ deviceSerialNumber ]
            self.write( '<li><a href="device/%s">%s</a></li>'
                        % ( deviceSerialNumber,
                            device[ 'name' ] ) )
        self.write( "</ul>" )
