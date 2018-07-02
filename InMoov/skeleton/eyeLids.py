# ##############################################################################
#            *** HEAD ***
# ##############################################################################


  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isEyeLidsActivated=0  
#read current skeleton part config
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

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
  
  if (isEyeLidsActivated and (ScriptType=="RightSide" or ScriptType=="LightSide" or ScriptType=="Full")) or ScriptType=="Virtual":
    EyeLidsConnectedToArduino=eval(ThisSkeletonPartConfig.get('MAIN', 'EyeLidsConnectedToArduino'))
except:
  isEyeLidsActivated=0
  errorSpokenFunc('ConfigParserProblem','eyelids . config')
  pass

  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if (isEyeLidsActivated and (ScriptType=="RightSide" or ScriptType=="LightSide" or ScriptType=="Full")) or ScriptType=="Virtual":
  if LeftPortIsConnected or RightPortIsConnected:
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
  
    i01.startEyelids(EyeLidsConnectedToArduino,ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyelidleft'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyelidright'))
    
    eyelids.eyelidleft.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyelidright'))
    eyelids.eyelidright.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyelidright'))
  
    eyelids.autoBlink(True)
    
       
  else:
    #we force parameter if arduino is off
    isEyeLidsActivated=0