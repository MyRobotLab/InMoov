# ##############################################################################
#            *** HEAD ***
# ##############################################################################



  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isEyeLidsActivated=0  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('eyeLids',ThisSkeletonPart+'.config')
###############################################################################

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isEyeLidsActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isEyeLidsActivated')
  EyeLidsLeftActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'EyeLidsLeftActivated') 
  EyeLidsRightActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'EyeLidsRightActivated') 
  
  if isEyeLidsActivated:
    EyeLidsConnectedToArduinoPort=eval(ThisSkeletonPartConfig.get('MAIN', 'EyeLidsConnectedToArduino').replace("left","MyLeftPort").replace("right","MyRightPort"))
    EyeLidsConnectedToArduino=eval(ThisSkeletonPartConfig.get('MAIN', 'EyeLidsConnectedToArduino'))
except:
  isEyeLidsActivated=0
  errorSpokenFunc('ConfigParserProblem','eyelids . config')
  pass
    
  
  
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isEyeLidsActivated==1:
  if LeftPortIsConnected or RighPortIsConnected:
    talkEvent(lang_startingEyeLids)
    eyelids = Runtime.create("i01.eyelids","InMoovEyelids")
        
    eyelids.eyelidleft.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyelidleft'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyelidleft'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyelidleft'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyelidleft')) 
    eyelids.eyelidright.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyelidright'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyelidright'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyelidright'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyelidright')) 
      
    eyelids.eyelidleft.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'eyelidleft'))
    eyelids.eyelidright.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'eyelidright'))

      
    eyelids.eyelidleft.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyelidleft'))
    eyelids.eyelidright.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyelidright'))
      
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyelidleft'):torso.eyelidleft.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyelidright'):torso.eyelidright.setInverted(True)
  
    i01.startEyelids(EyeLidsConnectedToArduinoPort)
    eyelids.eyelidleft.enableAutoEnable(1)
    eyelids.eyelidright.enableAutoEnable(1)
    eyelids.eyelidleft.enableAutoDisable(0)
    eyelids.eyelidright.enableAutoDisable(0)
  
    eyelids.rest()
       
  else:
    #we force parameter if arduino is off
    isEyeLidsActivated=0
    
#todo set inverted
