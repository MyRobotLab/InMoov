# ##############################################################################
#            *** RIGHT HAND ***
# ##############################################################################

 
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
isRightHandActivated=0
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('rightHand',ThisSkeletonPart+'.config')
###############################################################################


try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isRightHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRightHandActivated') 
  
except:
  errorSpokenFunc('ConfigParserProblem','right hand . config')
  pass    
 
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isRightHandActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full") or ScriptType=="Virtual":
  isRightHandActivated=1
  if RightPortIsConnected:
    talkEvent(lang_startingRightHand)
    
    rightHand = Runtime.create("i01.rightHand", "InMoovHand")
        
    rightHand.thumb.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'thumb')) 
    rightHand.index.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'index')) 
    rightHand.majeure.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'majeure')) 
    rightHand.ringFinger.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'ringFinger')) 
    rightHand.pinky.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'pinky'))
    rightHand.wrist.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'wrist'))
    
  
    rightHand.thumb.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'thumb'))
    rightHand.index.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'index'))
    rightHand.majeure.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'majeure'))
    rightHand.ringFinger.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'ringFinger'))
    rightHand.pinky.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'pinky'))
    rightHand.wrist.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'wrist'))
        

        
    rightHand.thumb.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'thumb'))
    rightHand.index.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'index'))
    rightHand.majeure.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'majeure'))
    rightHand.ringFinger.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'ringFinger'))
    rightHand.pinky.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'pinky'))
    rightHand.wrist.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'wrist'))
    
    rightHand.thumb.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'thumb'))
    rightHand.index.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'index'))
    rightHand.majeure.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'majeure'))
    rightHand.ringFinger.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'ringFinger'))
    rightHand.pinky.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'pinky'))
    rightHand.wrist.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'wrist'))
    
    i01.startRightHand(MyRightPort,BoardTypeMyRightPort)

    rightHand.rest()
    
    rightHand.thumb.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'thumb'))
    rightHand.index.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'index'))
    rightHand.majeure.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'majeure'))
    rightHand.ringFinger.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'ringFinger'))
    rightHand.pinky.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'pinky'))
    rightHand.wrist.setAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'wrist'))
    
  else:
    #we force parameter if arduino is off
    isRightHandActivated=0