# ##############################################################################
#						*** RIGHT HAND PROGRAM ***
# ##############################################################################


# ##############################################################################
# 								EAR COMMANDS
# ##############################################################################

ear.addCommand("open your right hand", "python", "handopen")
ear.addCommand("close your right hand", "python", "handclose")
ear.addCommand("open your hand", "python", "handopen")
ear.addCommand("close your hand", "python", "handclose")

def handopen():
	attachDetachThread(rightHand,2)
	i01.moveHand("right",0,0,0,0,0)


def handclose():
	attachDetachThread(rightHand,2)
	i01.moveHand("right",180,180,180,180,180)
  
# end ear commands
  





  
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
CheckConfigFileExist(ThisSkeletonPart)
ThisSkeletonPartConfig = ConfigParser.ConfigParser()
ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

isRightHandActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRightHandActivated') 
  
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isRightHandActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	if RightPortIsConnected==True:
	
		i01.startRightHand(MyRightPort)
		rightHand=i01.rightHand
		
		rightHand.thumb.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'thumb'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'thumb')) 
		rightHand.index.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'index'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'index')) 
		rightHand.majeure.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'majeure'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'majeure')) 
		rightHand.ringFinger.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'ringFinger'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'ringFinger')) 
		rightHand.pinky.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'pinky'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'pinky'))
		rightHand.wrist.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'wrist'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'wrist'))
		
		rightHand.thumb.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'thumb'))
		rightHand.index.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'index'))
		rightHand.majeure.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'majeure'))
		rightHand.ringFinger.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'ringFinger'))
		rightHand.pinky.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'pinky'))
		rightHand.wrist.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'wrist'))
		
		
	else:
		#we force parameter if arduino is off
		isRightHandActivated=0
		
#todo set inverted
