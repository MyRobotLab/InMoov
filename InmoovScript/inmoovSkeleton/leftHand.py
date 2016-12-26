# ##############################################################################
#						*** LEFT HAND PROGRAM ***
# ##############################################################################


# ##############################################################################
# 								EAR COMMANDS
# ##############################################################################

ear.addCommand("open your left hand", "python", "lefthandopen")
ear.addCommand("close your left hand", "python", "lefthandclose")


def lefthandopen():
	attachDetachThread(leftHand,2)
	i01.moveHand("left",0,0,0,0,0)


def lefthandclose():
	attachDetachThread(leftHand,2)
	i01.moveHand("left",180,180,180,180,180)
  
# end ear commands
  





  
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
CheckConfigFileExist(ThisSkeletonPart)
ThisSkeletonPartConfig = ConfigParser.ConfigParser()
ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

isLeftHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftHandActivated') 
  
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isLeftHandActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected==True:
	
		i01.startLeftHand(MyLeftPort)
		leftHand=i01.leftHand
		
		leftHand.thumb.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'thumb')) 
		leftHand.index.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'index')) 
		leftHand.majeure.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'majeure')) 
		leftHand.ringFinger.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'ringFinger')) 
		leftHand.pinky.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'pinky'))
		leftHand.wrist.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'wrist'))
		
		leftHand.thumb.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'thumb'))
		leftHand.index.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'index'))
		leftHand.majeure.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'majeure'))
		leftHand.ringFinger.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'ringFinger'))
		leftHand.pinky.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'pinky'))
		leftHand.wrist.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'wrist'))
		
		
	else:
		#we force parameter if arduino is off
		isleftHandActivated=0
		
#todo set inverted
