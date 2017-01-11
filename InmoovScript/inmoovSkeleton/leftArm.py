# ##############################################################################
#						*** LEFT ARM ***
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

	isLeftArmActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isLeftArmActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')

except:
	errorSpokenFunc('ConfigParserProblem','leftarm.config')
	pass
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isLeftArmActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected==True:
		talkEvent(lang_startingLeftArm)
		
		leftArm = Runtime.create("i01.leftArm", "InMoovArm")
		
		try:			
			leftArm.bicep.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'bicep'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'bicep'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'bicep')) 
			leftArm.shoulder.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'shoulder'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'shoulder'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'shoulder')) 
			leftArm.rotate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'rotate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'rotate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'rotate')) 
			leftArm.omoplate.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'omoplate'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'omoplate'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'omoplate')) 
		
			leftArm.bicep.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'bicep'))
			leftArm.shoulder.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'shoulder'))
			leftArm.rotate.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'rotate'))
			leftArm.omoplate.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'omoplate'))

			leftArm.bicep.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'bicep'))
			leftArm.shoulder.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'shoulder'))
			leftArm.rotate.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'rotate'))
			leftArm.omoplate.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'omoplate'))
		except:
			errorSpokenFunc('ConfigParserProblem',ThisSkeletonPart)
			pass
			
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'bicep'):
			leftArm.bicep.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'shoulder'):
			leftArm.shoulder.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rotate'):
			leftArm.rotate.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'omoplate'):
			leftArm.omoplate.setInverted(True)
		
		i01.startLeftArm(MyLeftPort)
		
		if autoDetach:
			leftArm.bicep.enableAutoAttach(1)
			leftArm.shoulder.enableAutoAttach(1)
			leftArm.rotate.enableAutoAttach(1)
			leftArm.omoplate.enableAutoAttach(1)

		leftArm.rest()
		sleep(3)
		leftArm.detach()
	else:
		#we force parameter if arduino is off
		isLeftArmActivated=0
		
#todo set inverted
