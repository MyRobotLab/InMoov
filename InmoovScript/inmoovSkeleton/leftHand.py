# ##############################################################################
#						*** LEFT HAND PROGRAM ***
# ##############################################################################


# ##############################################################################
# 								EAR COMMANDS
# ##############################################################################

ear.addCommand("open your left hand", "python", "lefthandopen")
ear.addCommand("close your left hand", "python", "lefthandclose")


def lefthandopen():
	i01.moveHand("left",0,0,0,0,0)


def lefthandclose():
	i01.moveHand("left",180,180,180,180,180)
  
# end ear commands
  





  
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
CheckFileExist(ThisSkeletonPart)
ThisSkeletonPartConfig = ConfigParser.ConfigParser()
ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

isLeftHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftHandActivated') 
autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')   
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isLeftHandActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected:
	
		leftHand = Runtime.create("i01.leftHand", "InMoovHand")
				
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
		
		leftHand.thumb.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'thumb'))
		leftHand.index.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'index'))
		leftHand.majeure.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'majeure'))
		leftHand.ringFinger.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'ringFinger'))
		leftHand.pinky.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'pinky'))
		leftHand.wrist.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'wrist'))
		
		i01.startLeftHand(MyLeftPort)
		
		if autoDetach:
			leftHand.thumb.enableAutoAttach(1)
			leftHand.index.enableAutoAttach(1)
			leftHand.majeure.enableAutoAttach(1)
			leftHand.ringFinger.enableAutoAttach(1)
			leftHand.pinky.enableAutoAttach(1)
			leftHand.wrist.enableAutoAttach(1)
		
		leftHand.rest()
		sleep(1)
		leftHand.detach()
	else:
		#we force parameter if arduino is off
		isleftHandActivated=0
		
#todo set inverted
