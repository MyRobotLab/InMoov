# ##############################################################################
#						*** HEAD ***
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

	isHeadActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isHeadActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
	MouthControlActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'MouthControlActivated')
except:
	errorSpokenFunc('ConfigParserProblem','head.config')
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isHeadActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected:
		talkEvent(lang_startingHead)
		head = Runtime.create("i01.head","InMoovHead")
				
		head.jaw.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'jaw'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'jaw')) 
		head.eyeX.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'eyeX'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'eyeX')) 
		head.eyeY.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'eyeY'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'eyeY')) 
		head.neck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'neck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'neck')) 
		head.rothead.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'rothead'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'rothead'))
		
		
		head.jaw.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'jaw'))
		head.eyeX.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'eyeX'))
		head.eyeY.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'eyeY'))
		head.neck.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'neck'))
		head.rothead.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'rothead'))

		
		head.jaw.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'jaw'))
		head.eyeX.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'eyeX'))
		head.eyeY.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'eyeY'))
		head.neck.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'neck'))
		head.rothead.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'rothead'))
	
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'jaw'):
			head.jaw.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyeX'):
			head.eyeX.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyeY'):
			head.eyeY.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'neck'):
			head.neck.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rothead'):
			head.rothead.setInverted(True)

		
		i01.startHead(MyLeftPort)
		if MouthControlActivated:
			i01.startMouthControl(MyLeftPort)
			i01.mouthControl.setmouth(ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'jaw'))
		
		head.jaw.enableAutoAttach(1)	
		if autoDetach:
			
			head.eyeX.enableAutoAttach(1)
			head.eyeY.enableAutoAttach(1)
			head.neck.enableAutoAttach(1)
			head.rothead.enableAutoAttach(1)
			
		
		head.rest()
		sleep(1)
		head.detach()
		
		
	else:
		#we force parameter if arduino is off
		isHeadActivated=0
		
#todo set inverted
