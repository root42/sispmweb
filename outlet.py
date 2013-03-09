import tornado.web
import sispm

class Outlet:
    def __init__( self,
                  outletParentDevice,
                  outletNumber,
                  outletDescription ):
        self.parentDevice = outletParentDevice
        self.number = outletNumber
        self.description = outletDescription

    def status( self ):
        return sispm.SisPM.outletStatus( outletParentDevice.deviceNumber,
                                         outletNumber )

class OutletHandler( tornado.web.RequestHandler ):
    def get( self ):
        self.write( "<h1>OutletHandler</h1>" )
        self.write( self )

