# ##############################################################################
#						*** RIGHT HAND PROGRAM ***
# ##############################################################################


# ##############################################################################
# 								BASIC EAR COMMANDS
# ##############################################################################

ear.addCommand("raise your right biceps", "python", "rightbicepsraise")
ear.addCommand("lower the right biceps", "python", "rightbicepslower")


def rightbicepsraise():
	i01.moveArm("left",0,0,0,0,0)

def rightbicepslower():
	i01.moveArm("left",180,180,180,180,180)
  
# end ear commands
  





  
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
CheckFileExist(ThisSkeletonPart)
ThisSkeletonPartConfig = ConfigParser.ConfigParser()
ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

isRightArmActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRightArmActivated') 
autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach') 
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isRightArmActivated==1 and (ScriptType=="RightSide" or ScriptType=="Full"):
	if RightPortIsConnected:
	
		rightArm = Runtime.create("i01.rightArm", "InMoovArm")
				
		rightArm.bicep.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'bicep')) 
		rightArm.shoulder.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'shoulder')) 
		rightArm.rotate.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'rotate')) 
		rightArm.omoplate.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'omoplate')) 
	
		rightArm.bicep.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'bicep'))
		rightArm.shoulder.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'shoulder'))
		rightArm.rotate.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'rotate'))
		rightArm.omoplate.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'omoplate'))

		rightArm.bicep.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'bicep'))
		rightArm.shoulder.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'shoulder'))
		rightArm.rotate.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'rotate'))
		rightArm.omoplate.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'omoplate'))

		i01.startRightArm(MyRightPort)
		
		if autoDetach:
			rightArm.bicep.enableAutoAttach(1)
			rightArm.shoulder.enableAutoAttach(1)
			rightArm.rotate.enableAutoAttach(1)
			rightArm.omoplate.enableAutoAttach(1)

		rightArm.rest()
		sleep(1)
		rightArm.detach()
	else:
		#we force parameter if arduino is off
		isRightArmActivated=0
		
#todo set inverted
