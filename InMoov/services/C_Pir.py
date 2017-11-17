# ##############################################################################
#            *** PIR SENSOR ***
# ##############################################################################

# exemple after 5 minutes of inactivity we call the function sleepModeSleep()
# and if human is detected and if the robot sleeping we call sleepModeWakeUp()


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('pir',ThisServicePart+'.config')
###############################################################################

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isPirActivated=0

isPirActivated=ThisServicePartConfig.getboolean('MAIN', 'isPirActivated') 
PirPin=ThisServicePartConfig.getint('MAIN', 'PirPin') 
if ScriptType=="Virtual":PirPin=2
PirArduino=ThisServicePartConfig.get('MAIN', 'PirControlerArduino')
PlayCurstomSoundIfDetection=ThisServicePartConfig.getboolean('MAIN', 'PlayCurstomSoundIfDetection')

# ##############################################################################
#                 SERVICE START
# ##############################################################################
#pir timer to avoid human detection notification every seconds...


#analog pin listener read the pir
def publishPinPir(pins):
  

  for pin in range(0, len(pins)):
    
    #human detected
    if pins[pin].value>0:
      if not i01.RobotIsSleeping and i01.RobotIsStarted:
        humanDetected()
      
      #wakeup action
      if i01.RobotIsSleeping:
        PirControlerArduino.disablePin(PirPin)
        sleepModeWakeUp()


if isPirActivated:
  try:
    PirControlerArduino=eval(PirArduino)
    talkEvent(lang_startingPir)
        
  except:
    errorSpokenFunc('BAdrduinoChoosen','pir')
    isPirActivated=0
    pass