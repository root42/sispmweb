import commands
import re

class SisPM:
    
    binary = "/usr/bin/sispmctl"
    listOfDevices = {}

    @staticmethod
    def statusOfOutlets( serialNumber ):
        status = {}
        command = '%s -D %s -g all' % ( SisPM.binary,
                                        serialNumber )
        result = commands.getoutput( command )
        for line in result.split( '\n' ):
            if len( line ) > 0:
                tokens = [ x.strip() for x in line.split( ':', 1 ) ]
                match = re.match( r'Status of outlet (.*)', tokens[ 0 ] )
                if match != None and len( match.groups() ) > 0:
                    if tokens[ 1 ] == 'on':
                        status[ match.group( 1 ) ] = True
                    else:
                        status[ match.group( 1 ) ] = False
        return status

    @staticmethod
    def initializeListOfDevices():
        listOfDevices = {}
        command = "%s -s" % ( SisPM.binary )
        result = commands.getoutput( command )
        currentDevice = {}
        for line in result.split( '\n' ):
            if len( line ) == 0:
                SisPM.listOfDevices[ currentDevice[ 'serialNumber' ] ] = currentDevice
            else:
                tokens = [ x.strip() for x in line.split( ':', 1 ) ]
                if len( tokens ) == 1:
                    currentDevice[ 'name' ] = tokens[ 0 ]
                elif tokens[ 0 ] == 'device type':
                    currentDevice[ 'description' ] = tokens[ 1 ]
                elif tokens[ 0 ] == 'serial number':
                    currentDevice[ 'serialNumber' ] = tokens[ 1 ]
                    
