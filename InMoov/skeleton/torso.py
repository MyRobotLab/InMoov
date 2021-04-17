# ##############################################################################
#            *** TORSO ***
# ##############################################################################

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

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
    torso = Runtime.create("i01.torso","InMoovTorso")
    torso.startPeers()
        
    torso.topStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'topStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'topStom')) 
    torso.midStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'midStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'midStom'))
    torso.lowStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'lowStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'lowStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'lowStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'lowStom')) 
    
    torso.topStom.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'topStom'))
    torso.midStom.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'midStom'))
    torso.lowStom.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'lowStom'))
    
    torso.topStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'topStom'))
    torso.midStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'midStom'))
    torso.lowStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'lowStom'))
      
    torso.topStom.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'topStom'))
    torso.midStom.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'midStom'))
    torso.lowStom.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'lowStom'))

    
    i01.startTorso(TorsoConnectedToArduinoPort,TorsoConnectedToArduinoPortBoardType)

    torso.rest()
    
    torso.topStom.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'topStom'))
    torso.midStom.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'midStom'))
    torso.lowStom.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'lowStom'))

       
  else:
    #we force parameter if arduino is off
    istorsoActivated=0
