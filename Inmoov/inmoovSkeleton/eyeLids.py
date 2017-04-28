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
    
try:
  test=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyelidleft')
except:
  ThisSkeletonPartConfig.add_section('SERVO_AUTO_DISABLE')
  ThisSkeletonPartConfig.set('SERVO_AUTO_DISABLE', 'eyelidleft', 1)
  ThisSkeletonPartConfig.set('SERVO_AUTO_DISABLE', 'eyelidright', 1)
  
  
  with open(ThisSkeletonPart+'.config', 'wb') as f:
    ThisSkeletonPartConfig.write(f)
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
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
      
    eyelids.eyelidleft.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyelidleft'))
    eyelids.eyelidright.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyelidright'))
  
 
    i01.startEyelids(EyeLidsConnectedToArduinoPort,ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyelidleft'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyelidright'))
    
    eyelids.eyelidleft.enableAutoEnable(1)
    eyelids.eyelidright.enableAutoEnable(1)
    eyelids.eyelidleft.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyelidright'))
    eyelids.eyelidright.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyelidright'))
  
    eyelids.rest()
       
  else:
    #we force parameter if arduino is off
    isEyeLidsActivated=0
    
#todo set inverted
