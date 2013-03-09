import commands

class SisPM:
    
    binary = "/usr/bin/sispmctl"
    listOfDevices = []

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
    def initializeListOfDevices():
        command = "%s -s"
        result = commands.getoutput( command )
