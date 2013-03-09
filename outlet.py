import tornado.web
import sispm

class OutletHandler( tornado.web.RequestHandler ):
    def get( self ):
        self.write( "<h1>OutletHandler</h1>" )
        self.write( self )

