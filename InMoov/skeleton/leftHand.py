# ##############################################################################
#            *** LEFT HAND ***
# ##############################################################################



# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
isLeftHandActivated=0
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('lefthand',ThisSkeletonPart+'.config')
###############################################################################


try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isLeftHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftHandActivated') 
  
  
except:
  errorSpokenFunc('ConfigParserProblem','lefthand.config')
  pass  
  
  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isLeftHandActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full") or ScriptType=="Virtual":
  isLeftHandActivated=1
  if LeftPortIsConnected:
    talkEvent(lang_startingLeftHand)
    
    thumb = Runtime.createAndStart("i01.leftHand.thumb","Servo")
    index = Runtime.createAndStart("i01.leftHand.index","Servo")
    majeure = Runtime.createAndStart("i01.leftHand.majeure","Servo")
    ringFinger = Runtime.createAndStart("i01.leftHand.ringFinger","Servo")
    pinky = Runtime.createAndStart("i01.leftHand.pinky","Servo")
    wrist = Runtime.createAndStart("i01.leftHand.wrist","Servo")
    
    leftHand = Runtime.create("i01.leftHand", "InMoovHand")
    leftHand.thumb.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'thumb')) 
    leftHand.index.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'index')) 
    leftHand.majeure.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'majeure')) 
    leftHand.ringFinger.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'ringFinger')) 
    leftHand.pinky.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'pinky'))
    leftHand.wrist.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'wrist'))
    
    leftHand.thumb.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'thumb'))
    leftHand.index.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'index'))
    leftHand.majeure.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'majeure'))
    leftHand.ringFinger.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'ringFinger'))
    leftHand.pinky.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'pinky'))
    leftHand.wrist.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'wrist'))
     
    leftHand.thumb.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'thumb'))
    leftHand.index.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'index'))
    leftHand.majeure.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'majeure'))
    leftHand.ringFinger.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'ringFinger'))
    leftHand.pinky.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'pinky'))
    leftHand.wrist.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'wrist'))
    
    leftHand.thumb.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'thumb'))
    leftHand.index.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'index'))
    leftHand.majeure.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'majeure'))
    leftHand.ringFinger.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'ringFinger'))
    leftHand.pinky.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'pinky'))
    leftHand.wrist.setInverted(ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'wrist'))
 
    i01.startLeftHand(MyLeftPort,BoardTypeMyLeftPort)
    
    leftHand.enableAutoEnable(1)
    leftHand.thumb.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'thumb'))
    leftHand.index.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'index'))
    leftHand.majeure.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'majeure'))
    leftHand.ringFinger.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'ringFinger'))
    leftHand.pinky.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'pinky'))
    leftHand.wrist.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'wrist'))

    leftHand.rest()
    
  else:
    #we force parameter if arduino is off
    isleftHandActivated=0