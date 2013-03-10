import tornado.web
import sispm
import outlet

class DeviceHandler( tornado.web.RequestHandler ):
    @tornado.web.removeslash
    def get( self, deviceSerialNumber ):
        devices = sispm.SisPM.listOfDevices
        device = devices[ deviceSerialNumber ]
        self.write( '<h1>Outlets for %s</h1>' % ( device[ 'name' ] ) )
        self.write( '<p>%s</p>' % ( device[ 'description' ] ) )
        statusOfOutlets = sispm.SisPM.statusOfOutlets( deviceSerialNumber )
        self.write( "<ul>")
        for outlet in statusOfOutlets:
            self.write( '<li><a href="%s/outlet/%s">Outlet %s</a> <a href="%s/outlet/%s/status/%s">%s</a></li>'
                        % ( deviceSerialNumber,
                            outlet,
                            outlet,
                            deviceSerialNumber,
                            outlet,
                            'False' if statusOfOutlets[ outlet ] else 'True',
                            'on' if statusOfOutlets[ outlet ] else 'off' ) )
        self.write( "</ul>" )

class DevicesHandler( tornado.web.RequestHandler ):
    @tornado.web.removeslash
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
