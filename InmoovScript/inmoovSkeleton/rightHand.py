# ##############################################################################
#						*** RIGHT HAND ***
# ##############################################################################

 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isRightHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRightHandActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
except:
	errorSpokenFunc('ConfigParserProblem','leftarm.config')
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isRightHandActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	if RightPortIsConnected:
		talkEvent(lang_startingRightHand)
		
		rightHand = Runtime.create("i01.rightHand", "InMoovHand")
				
		rightHand.thumb.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'thumb')) 
		rightHand.index.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'index')) 
		rightHand.majeure.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'majeure')) 
		rightHand.ringFinger.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'ringFinger')) 
		rightHand.pinky.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'pinky'))
		rightHand.wrist.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'wrist'))
		
		rightHand.thumb.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'thumb'))
		rightHand.index.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'index'))
		rightHand.majeure.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'majeure'))
		rightHand.ringFinger.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'ringFinger'))
		rightHand.pinky.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'pinky'))
		rightHand.wrist.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'wrist'))
		
		rightHand.thumb.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'thumb'))
		rightHand.index.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'index'))
		rightHand.majeure.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'majeure'))
		rightHand.ringFinger.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'ringFinger'))
		rightHand.pinky.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'pinky'))
		rightHand.wrist.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'wrist'))
				
		rightHand.thumb.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'thumb'))
		rightHand.index.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'index'))
		rightHand.majeure.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'majeure'))
		rightHand.ringFinger.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'ringFinger'))
		rightHand.pinky.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'pinky'))
		rightHand.wrist.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'wrist'))
		
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'thumb'):
			rightHand.thumb.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'index'):
			rightHand.index.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'majeure'):
			rightHand.majeure.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'ringFinger'):
			rightHand.ringFinger.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'pinky'):
			rightHand.pinky.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'wrist'):
			rightHand.wrist.setInverted(True)
		
		i01.startRightHand(MyRightPort)
		
			
		if autoDetach:
			rightHand.thumb.enableAutoAttach(1)
			rightHand.index.enableAutoAttach(1)
			rightHand.majeure.enableAutoAttach(1)
			rightHand.ringFinger.enableAutoAttach(1)
			rightHand.pinky.enableAutoAttach(1)
			rightHand.wrist.enableAutoAttach(1)
		
		rightHand.detach()
		rightHand.thumb.attach(right,ThisSkeletonPartConfig.getint('SERVO_PIN', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'thumb'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'thumb'))
		rightHand.index.attach(right,ThisSkeletonPartConfig.getint('SERVO_PIN', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'index'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'index'))
		rightHand.majeure.attach(right,ThisSkeletonPartConfig.getint('SERVO_PIN', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'majeure'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'majeure'))
		rightHand.ringFinger.attach(right,ThisSkeletonPartConfig.getint('SERVO_PIN', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'ringFinger'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'ringFinger'))
		rightHand.pinky.attach(right,ThisSkeletonPartConfig.getint('SERVO_PIN', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'pinky'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'pinky'))
		rightHand.wrist.attach(right,ThisSkeletonPartConfig.getint('SERVO_PIN', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'wrist'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'wrist'))
		rightHand.attach()
		
	else:
		#we force parameter if arduino is off
		isRightHandActivated=0
		
#todo set inverted
