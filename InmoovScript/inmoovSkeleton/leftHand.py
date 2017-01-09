# ##############################################################################
#						*** LEFT HAND ***
# ##############################################################################

# Thumb------pin 2
# Index------pin 3
# Majeure----pin 4
# RingFinger-pin 5
# Pinky------pin 6
# wrist------pin 7  
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isLeftHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftHandActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
	
except:
	errorSpokenFunc('ConfigParserProblem','lefthand.config')
	pass	
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isLeftHandActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected:
		talkEvent(lang_startingLeftHand)
		leftHand = Runtime.create("i01.leftHand", "InMoovHand")
				
		leftHand.thumb.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'thumb'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'thumb')) 
		leftHand.index.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'index'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'index'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'index')) 
		leftHand.majeure.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'majeure'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'majeure')) 
		leftHand.ringFinger.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'ringFinger'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'ringFinger')) 
		leftHand.pinky.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'pinky'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'pinky'))
		leftHand.wrist.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'wrist'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'wrist'))
		
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
		
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'thumb'):
			leftHand.thumb.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'index'):
			leftHand.index.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'majeure'):
			leftHand.majeure.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'ringFinger'):
			leftHand.ringFinger.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'pinky'):
			leftHand.pinky.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'wrist'):
			leftHand.wrist.setInverted(True)
		
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
