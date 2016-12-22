# ##############################################################################
# 								RIGHT HAND
# ##############################################################################

#read right had config
RightHandConfig = ConfigParser.ConfigParser()
RightHandConfig.read(RuningFolder+'inmoovSkeleton/RightHand.config')

isRightHandActivated=RightHandConfig.getboolean('MAIN', 'isRightHandActivated')

#launch
if isRightHandActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	if RightPortIsConnected==True:
		rightHand = Runtime.create("i01.rightHand", "InMoovHand")
		rightHand.thumb.setMinMax(RightHandConfig.getint('SERVO_MINIMUM', 'thumb'),RightHandConfig.getint('SERVO_MAXIMUM', 'thumb')) 
		rightHand.index.setMinMax(RightHandConfig.getint('SERVO_MINIMUM', 'index'),RightHandConfig.getint('SERVO_MAXIMUM', 'index')) 
		rightHand.majeure.setMinMax(RightHandConfig.getint('SERVO_MINIMUM', 'majeure'),RightHandConfig.getint('SERVO_MAXIMUM', 'majeure')) 
		rightHand.ringFinger.setMinMax(RightHandConfig.getint('SERVO_MINIMUM', 'ringFinger'),RightHandConfig.getint('SERVO_MAXIMUM', 'ringFinger')) 
		rightHand.pinky.setMinMax(RightHandConfig.getint('SERVO_MINIMUM', 'pinky'),RightHandConfig.getint('SERVO_MAXIMUM', 'pinky')) 
		rightHand.wrist.setMinMax(RightHandConfig.getint('SERVO_MINIMUM', 'wrist'),RightHandConfig.getint('SERVO_MAXIMUM', 'wrist')) 
		
		rightHand.thumb.map(0,180,RightHandConfig.getint('SERVO_MINIMUM', 'thumb'),RightHandConfig.getint('SERVO_MAXIMUM', 'thumb')) 
		rightHand.index.map(0,180,RightHandConfig.getint('SERVO_MINIMUM', 'index'),RightHandConfig.getint('SERVO_MAXIMUM', 'index')) 
		rightHand.majeure.map(0,180,RightHandConfig.getint('SERVO_MINIMUM', 'majeure'),RightHandConfig.getint('SERVO_MAXIMUM', 'majeure')) 
		rightHand.ringFinger.map(0,180,RightHandConfig.getint('SERVO_MINIMUM', 'ringFinger'),RightHandConfig.getint('SERVO_MAXIMUM', 'ringFinger')) 
		rightHand.pinky.map(0,180,RightHandConfig.getint('SERVO_MINIMUM', 'pinky'),RightHandConfig.getint('SERVO_MAXIMUM', 'pinky'))
		rightHand.wrist.map(0,180,RightHandConfig.getint('SERVO_MINIMUM', 'wrist'),RightHandConfig.getint('SERVO_MAXIMUM', 'wrist'))
		
		rightHand.thumb.setVelocity(RightHandConfig.getint('DEF_SPEED', 'thumb'))
		rightHand.index.setVelocity(RightHandConfig.getint('DEF_SPEED', 'index'))
		rightHand.majeure.setVelocity(RightHandConfig.getint('DEF_SPEED', 'majeure'))
		rightHand.ringFinger.setVelocity(RightHandConfig.getint('DEF_SPEED', 'ringFinger'))
		rightHand.pinky.setVelocity(RightHandConfig.getint('DEF_SPEED', 'pinky'))
		rightHand.wrist.setVelocity(RightHandConfig.getint('DEF_SPEED', 'wrist'))
		
		i01.startRightHand(MyRightPort)
		rightHand=i01.rightHand
	else:
		#we force parameter if arduino is off
		isRightHandActivated=0
		
#todo set inverted
