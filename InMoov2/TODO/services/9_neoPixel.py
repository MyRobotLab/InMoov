# ##############################################################################
#            *** MRL SERVICE - NEOPIXEL  ***
# ##############################################################################

  #TODO ADD PIXEL MATRIX
  
  #Animations;
  #"Color Wipe"
  #"Larson Scanner"
  #"Theater Chase"
  #"Theater Chase Rainbow"
  #"Rainbow"
  #"Rainbow Cycle"
  #"Flash Random"
  #"Ironman" > bug ?

  #speed: 1-65535   1=full speed, 2=2x slower than 1, 10=10x slower than 1
  #starting a animation :
##  neopixel.setAnimation("Animation Name", red, green, blue, speed)
##  optional : i01.setNeopixelAnimation("Animation Name", red, green, blue, speed, duration) > animation timeout, if neopixel exist

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('Neopixel',ThisServicePart+'.config')
###############################################################################

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isNeopixelActivated=0



try:
    flash_when_speak = ThisServicePartConfig.getboolean('BASIC_REACTIONS', 'flash_when_speak')
except:
  flash_when_speak=0
  ThisServicePartConfig.set('BASIC_REACTIONS', 'flash_when_speak', 0)
  with open(ThisServicePart+'.config', 'wb') as f:
    ThisServicePartConfig.write(f)
  pass


try:
  isNeopixelActivated=ThisServicePartConfig.getboolean('MAIN', 'isNeopixelActivated') 
  masterArduinoPort=ThisServicePartConfig.get('MAIN', 'NeopixelMasterPort')
  pin=ThisServicePartConfig.getint('NEOPIXEL', 'pin') 
  numberOfPixel=ThisServicePartConfig.getint('NEOPIXEL', 'numberOfPixel')

  #neopixel can have basic pre programmed reactions:
  #TODO choose witch animation

  #light green while robot booting
  boot_green=ThisServicePartConfig.getboolean('BASIC_REACTIONS', 'boot_green')
  #blue while download something
  downloadSomething_blue=ThisServicePartConfig.getboolean('BASIC_REACTIONS', 'downloadSomething_blue')

  error_red=ThisServicePartConfig.getboolean('BASIC_REACTIONS', 'error_red')
except:
  errorSpokenFunc('ConfigParserProblem','Neopixel.config')
  pass
  
#for noworky
log.info("NEOPIXEL.config")
log.info("NeopixelMaster : "+str(ThisServicePartConfig.get('MAIN', 'NeopixelMaster')))
log.info("masterArduinoPort : "+str(masterArduinoPort))
log.info("isNeopixelActivated : "+str(isNeopixelActivated))
log.info("pin : "+str(pin))
log.info("numberOfPixel : "+str(numberOfPixel))
  
# ##############################################################################
#                 SERVICE START
# ##############################################################################

if isNeopixelActivated==1:
  neopixelArduino = Runtime.createAndStart("neopixelArduino","Arduino")
  neopixelArduino.usedByInmoov=True
  neopixelArduino.serial.usedByInmoov=True
  
  #check if connection is serial or usb
  if masterArduinoPort[:3].lower()=="com" or masterArduinoPort[:4].lower()=="/dev":
    neopixelArduinoIsConnected=CheckArduinos(neopixelArduino,masterArduinoPort)
  else:
    try:
      masterArduino=eval(ThisServicePartConfig.get('MAIN', 'NeopixelMaster'))
      neopixelArduinoIsConnected=CheckArduinos(neopixelArduino,masterArduinoPort,masterArduino)
    except:
      errorSpokenFunc('BAdrduinoChoosen','Neo pixel')
      isNeopixelActivated=0
      neopixelArduinoIsConnected=0
      pass  
  
  
  sleep(0.1)

  neopixel = Runtime.createAndStart("neopixel","NeoPixel")
  if neopixelArduinoIsConnected==True:
    #Starting NeoPixel Service
    neopixel.attach(neopixelArduino, pin, numberOfPixel)
    i01.neopixel=neopixel
    i01.neopixelArduino=neopixelArduino
    talkEvent(lang_startingNeoPixel)
  else:
    isNeopixelActivated=0
    
if boot_green and isNeopixelActivated:    
  i01.setNeopixelAnimation("Theater Chase", 0, 255, 50, 1)