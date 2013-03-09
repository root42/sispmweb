import commands

class SisPM:
    
    binary = "/usr/bin/sispmctl"
    listOfDevices = {}

    @staticmethod
    def outletStatus( deviceNumber,
                      deviceSerialNumber,
                      outletNumber ):
        command = ""
        if deviceNumber != None:
            command = "%s -q -d %u -g %u" % ( SisPM.binary,
                                              deviceNumber,
                                              outletNumber )
        elif deviceSerialNumber != None:
            command = "%s -q -D %u -g %u" % ( SisPM.binary,
                                              deviceSerialNumber,
                                              outletNumber )
        else:
            return None

        result = commands.getoutput( command )
        if result == "0":
            return False
        elif result == "1":
            return True
        else:
            return None

    @staticmethod
    def statusOfOutlets( serialNumber ):
        return "Not yet implemented"

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
                    
