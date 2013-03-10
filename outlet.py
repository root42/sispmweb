import tornado.web
import sispm

class OutletHandler( tornado.web.RequestHandler ):
    @tornado.web.removeslash
    def get( self,
             deviceSerialNumber,
             outletNumber ):
        devices = sispm.SisPM.listOfDevices
        device = devices[ deviceSerialNumber ]
        statusOfOutlets = sispm.SisPM.statusOfOutlets( deviceSerialNumber )
        self.write( "<h1>OutletHandler</h1>" )
        self.write( "Outlet %s is %s" % ( outletNumber,
                                          'on' if statusOfOutlets[ outletNumber ] else 'off' ) )

class OutletStatusHandler( tornado.web.RequestHandler ):
    def get( self,
             deviceSerialNumber,
             outletNumber,
             outletStatus ):
        status = True if outletStatus == 'True' else False
        result = sispm.SisPM.setStatusOfOutlet( deviceSerialNumber,
                                                outletNumber,
                                                status )
        # send user back to the current device overview
        self.redirect( '../../../' )

