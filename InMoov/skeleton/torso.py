# ##############################################################################
#            *** TORSO ***
# ##############################################################################

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('torso',ThisSkeletonPart+'.config')
###############################################################################


isTorsoActivated=0
try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isTorsoActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isTorsoActivated') 
  
  if isTorsoActivated or ScriptType=="Virtual":
    TorsoConnectedToArduinoPort=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino').replace("left","MyLeftPort").replace("right","MyRightPort"))
    TorsoConnectedToArduino=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino'))
    TorsoConnectedToArduinoPortBoardType=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino').replace("left","BoardTypeMyLeftPort").replace("right","BoardTypeMyRightPort"))
except:
  errorSpokenFunc('ConfigParserProblem','torso.config')
  isTorsoActivated=0
  TorsoConnectedToArduino=""
  pass

# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isTorsoActivated or ScriptType=="Virtual":
  if LeftPortIsConnected or RightPortIsConnected  or ScriptType=="Virtual":
    isTorsoActivated=1
    talkEvent(lang_startingTorso)
    torso = Runtime.create("i01.torso","InMoovTorso")
        
    torso.topStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'topStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'topStom')) 
    torso.midStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'midStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'midStom')) 
    
    torso.topStom.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'topStom'))
    torso.midStom.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'midStom'))
    torso.lowStom.setMaxVelocity(-1)
    
    torso.topStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'topStom'))
    torso.midStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'midStom'))
      
    torso.topStom.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'topStom'))
    torso.midStom.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'midStom'))
    
    i01.startTorso(TorsoConnectedToArduinoPort,TorsoConnectedToArduinoPortBoardType)

    torso.rest()
    
    torso.topStom.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'topStom'))
    torso.midStom.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'midStom'))
       
  else:
    #we force parameter if arduino is off
    istorsoActivated=0