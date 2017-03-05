# ##############################################################################
#						*** TORSO ***
# ##############################################################################


 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
isTorsoActivated=0
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isTorsoActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isTorsoActivated') 
	
	if isTorsoActivated:
		TorsoConnectedToArduinoPort=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino').replace("left","MyLeftPort").replace("right","MyRightPort"))
		TorsoConnectedToArduino=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino'))
except:
	errorSpokenFunc('ConfigParserProblem','torso.config')
	isTorsoActivated=0
	TorsoConnectedToArduino=""
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isTorsoActivated and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected:
		talkEvent(lang_startingTorso)
		torso = Runtime.create("i01.torso","InMoovTorso")
				
		torso.topStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'topStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'topStom')) 
		torso.midStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'midStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'midStom')) 
		
		torso.topStom.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'topStom'))
		torso.midStom.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'midStom'))
		
		torso.topStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'topStom'))
		torso.midStom.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'midStom'))
			
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'topStom'):torso.topStom.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'midStom'):torso.midStom.setInverted(True)
		
		
		
		i01.startTorso(TorsoConnectedToArduinoPort)
		torso.detach()
		torso.topStom.attach(TorsoConnectedToArduino,ThisSkeletonPartConfig.getint('SERVO_PIN', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'topStom'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'topStom'))
		torso.midStom.attach(TorsoConnectedToArduino,ThisSkeletonPartConfig.getint('SERVO_PIN', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'midStom'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'midStom'))
		
		torso.attach()
		
		torso.topStom.enableAutoAttach(1)
		torso.midStom.enableAutoAttach(1)
		torso.topStom.enableAutoDetach(0)
		torso.midStom.enableAutoDetach(0)
	
		torso.rest()
		
		
	else:
		#we force parameter if arduino is off
		istorsoActivated=0
		
#todo set inverted
