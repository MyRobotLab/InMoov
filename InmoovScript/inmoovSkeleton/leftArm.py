# ##############################################################################
#						*** LEFT HAND PROGRAM ***
# ##############################################################################


# ##############################################################################
# 								BASIC EAR COMMANDS
# ##############################################################################

ear.addCommand("attach left arm", "i01.leftArm", "attach")
ear.addCommand("disconnect left arm", "i01.leftArm", "detach")

  
# end ear commands
  





  
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
CheckFileExist(ThisSkeletonPart)
ThisSkeletonPartConfig = ConfigParser.ConfigParser()
ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

isLeftArmActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftArmActivated') 
autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach') 
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isLeftArmActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected==True:
	
		leftArm = Runtime.create("i01.leftArm", "InMoovArm")
				
		leftArm.bicep.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'bicep')) 
		leftArm.shoulder.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'shoulder')) 
		leftArm.rotate.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'rotate')) 
		leftArm.omoplate.map(0,180,ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'omoplate')) 
	
		leftArm.bicep.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'bicep'))
		leftArm.shoulder.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'shoulder'))
		leftArm.rotate.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'rotate'))
		leftArm.omoplate.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'omoplate'))

		leftArm.bicep.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'bicep'))
		leftArm.shoulder.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'shoulder'))
		leftArm.rotate.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'rotate'))
		leftArm.omoplate.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'omoplate'))
		
		i01.startLeftArm(MyLeftPort)
		
		if autoDetach:
			leftArm.bicep.enableAutoAttach(1)
			leftArm.shoulder.enableAutoAttach(1)
			leftArm.rotate.enableAutoAttach(1)
			leftArm.omoplate.enableAutoAttach(1)

		leftArm.rest()
		sleep(1)
		leftArm.detach()
	else:
		#we force parameter if arduino is off
		isLeftArmActivated=0
		
#todo set inverted
