# ##############################################################################
#                 ARDUINO SERVICE FILE
# ##############################################################################


# ##############################################################################
# ARDUINO RELATED FUNCTIONS
# ##############################################################################

#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
MyRightPort=ThisServicePartConfig.get('MAIN', 'MyRightPort')
MyLeftPort=ThisServicePartConfig.get('MAIN', 'MyLeftPort')
BoardTypeMyRightPort=ThisServicePartConfig.get('MAIN', 'BoardTypeMyRightPort')
BoardTypeMyLeftPort=ThisServicePartConfig.get('MAIN', 'BoardTypeMyLeftPort')
ForceArduinoIsConnected=ThisServicePartConfig.getboolean('MAIN', 'ForceArduinoIsConnected')
ArefLeftArduino=ThisServicePartConfig.get('MAIN', 'ArefLeftArduino')
ArefRightArduino=ThisServicePartConfig.get('MAIN', 'ArefRightArduino')
  
#for noworky
log.info("ARDUINO.config")
log.info("MyRightPort : "+str(MyRightPort))
log.info("MyLeftPort : "+str(MyLeftPort))
log.info("BoardTypeMyRightPort : "+str(BoardTypeMyRightPort))
log.info("BoardTypeMyLeftPort : "+str(BoardTypeMyLeftPort))
log.info("ArefLeftArduino : "+str(ArefLeftArduino))
log.info("ArefRightArduino : "+str(ArefRightArduino))
#function to check arduino & mrlcomm
def CheckArduinos(Card,Port,slave=0):
  
  #serial
  if slave!=0:
    Card.connect(slave,Port)
    sleep(1)
    for i in range(0,3):
      if not Card.isConnected():
        Card.disconnect()
        sleep(0.1)
        Card.connect(slave,Port)
        sleep(0.5)
      else:
        break
        
  #usb
  else:
    Card.connect(Port)
    sleep(1)
    for i in range(0,3):
      if not Card.isConnected():
        Card.disconnect()
        sleep(0.1)
        Card.connect(Port)
        sleep(0.5)
      else:
        break
    
  if ForceArduinoIsConnected:return True
  else:
  
    #mrlcomm check
    if Card.isConnected():
      print "Mrlcomm version : ",Card.getBoardInfo().version," ( requiered ",MRLCOMM_VERSION," )"
      if Card.getBoardInfo().version!=MRLCOMM_VERSION:errorSpokenFunc('BadMrlcommVersion',Port)
      else:
        print "Arduino ",Port," OK"
        return True
    else:
      #bouuuuuhhhh
      errorSpokenFunc('ArduinoNotConnected',Port)
      return False