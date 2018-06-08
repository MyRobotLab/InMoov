# ##############################################################################
#            *** NERVOBOARD RELAY  ***
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name

ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isNervoboardRelayActivated=0

isNervoboardRelayActivated=ThisServicePartConfig.getboolean('MAIN', 'isNervoboardRelayActivated') 

PinLeftNervoPower1=0
PinRightNervoPower1=0

try:
  PinLeftNervoPower1=ThisServicePartConfig.getint('MAIN', 'PinLeftNervoPower1') 
  PinRightNervoPower1=ThisServicePartConfig.getint('MAIN', 'PinRightNervoPower1') 
except:
  pass
  
# ##############################################################################
#                 SERVICE START
# ##############################################################################

def switchOnAllNervo():
  if isNervoboardRelayActivated:
    i01.LeftRelay1.on()
    i01.RightRelay1.on()

def switchOffAllNervo():
  if isNervoboardRelayActivated:
    i01.LeftRelay1.off()
    i01.RightRelay1.off()


if isNervoboardRelayActivated:
  try:
    NervoboardRelayControlerArduino=eval(ThisServicePartConfig.get('MAIN', 'NervoboardRelayControlerArduino'))
    talkEvent(lang_startingNervoPower)
    i01.LeftRelay1=Runtime.createAndStart("i01.LeftRelay1", "Relay")
    i01.LeftRelay1.arduino=NervoboardRelayControlerArduino
    i01.LeftRelay1.pin=PinLeftNervoPower1

    i01.RightRelay1=Runtime.createAndStart("i01.RightRelay1", "Relay")
    i01.RightRelay1.arduino=NervoboardRelayControlerArduino
    i01.RightRelay1.pin=PinRightNervoPower1
    
    switchOnAllNervo()
  except:
    errorSpokenFunc('BAdrduinoChoosen','nervo board relay')
    isNervoboardRelayActivated=0
    pass
      
  