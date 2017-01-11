# ##############################################################################
#						*** TORSO ***
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

	isTorsoActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isTorsoActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
	TorsoConnectedToArduino=eval(ThisSkeletonPartConfig.get('MAIN', 'TorsoConnectedToArduino').replace("left","MyLeftPort").replace("right","MyRightPort"))

except:
	errorSpokenFunc('ConfigParserProblem','torso.config')
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isTorsoActivated and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected:
		talkEvent(lang_startingTorso)
		torso = Runtime.create("i01.torso","InMoovTorso")
				
		torso.topStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'topStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'topStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'topStom')) 
		torso.midStom.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP', 'midStom'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM', 'midStom'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM', 'midStom')) 
		
		torso.topStom.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'topStom'))
		torso.midStom.setVelocity(ThisSkeletonPartConfig.getint('DEF_SPEED', 'midStom'))
		
		torso.topStom.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'topStom'))
		torso.midStom.setRest(ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'midStom'))
			
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'topStom'):
			torso.topStom.setInverted(True)
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'midStom'):
			torso.midStom.setInverted(True)
		
		
		
		i01.startTorso(TorsoConnectedToArduino)
		
		
		if autoDetach:
			torso.topStom.enableAutoAttach(1)
			torso.midStom.enableAutoAttach(1)
		
		torso.rest()
		sleep(3)
		torso.detach()
		
		
	else:
		#we force parameter if arduino is off
		istorsoActivated=0
		
#todo set inverted
