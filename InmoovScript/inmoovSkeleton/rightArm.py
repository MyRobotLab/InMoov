# ##############################################################################
#            *** RIGHT ARM ***
# ##############################################################################



  
  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
isRightArmActivated=0
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('rightArm',ThisSkeletonPart+'.config')
###############################################################################


try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isRightArmActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRightArmActivated') 
  

except:
  errorSpokenFunc('ConfigParserProblem','rightarm.config')
  pass  
# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isRightArmActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full" or ScriptType=="Virtual"):
  if RightPortIsConnected:
    talkEvent(lang_startingRightArm)
    rightArm = Runtime.create("i01.rightArm", "InMoovArm")
        
    rightArm.bicep.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'bicep'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'bicep')) 
    rightArm.shoulder.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'shoulder'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'shoulder')) 
    rightArm.rotate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rotate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rotate')) 
    rightArm.omoplate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'omoplate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'omoplate')) 
    
  
    rightArm.bicep.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'bicep'))
    rightArm.shoulder.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'shoulder'))
    rightArm.rotate.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rotate'))
    rightArm.omoplate.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'omoplate'))

    rightArm.bicep.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'bicep'))
    rightArm.shoulder.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'shoulder'))
    rightArm.rotate.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rotate'))
    rightArm.omoplate.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'omoplate'))
    
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'bicep'):rightArm.bicep.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'shoulder'):rightArm.shoulder.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rotate'):rightArm.rotate.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'omoplate'):rightArm.omoplate.setInverted(True)

    i01.startRightArm(MyRightPort)
    
    rightArm.enableAutoEnable(1)
    rightArm.enableAutoEnable(0)

    
    rightArm.rest()

  else:
    #we force parameter if arduino is off
    isRightArmActivated=0
    
#todo set inverted
