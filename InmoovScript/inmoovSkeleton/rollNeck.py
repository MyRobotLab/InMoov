# ##############################################################################
#						*** MOD ROLLNECK ***
# ##############################################################################


 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
isRollNeckActivated=0  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')

try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isRollNeckActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isRollNeckActivated') 
	RollNeckArduino=ThisSkeletonPartConfig.get('ARDUINO', 'RollNeckArduino')
	RollNeckPin=ThisSkeletonPartConfig.getint('ARDUINO', 'RollNeckPin')
	RollNeckRestPosition=ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rollneck')
	RollNeckMaxVelocity=ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rollneck')
	
except:
	errorSpokenFunc('ConfigParserProblem','rollneck.config')
	pass
    
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isRollNeckActivated==1 and (ScriptType!="NoArduino"):

# ##############################################################################
# 								ARDUINO CHECK
# ##############################################################################
	masterArduinoRollNeckIsconnected=0
	try:
		
		
		if RollNeckArduino=="left":
			masterArduinoRollNeckIsconnected=LeftPortIsConnected
		if RollNeckArduino=="right":
			masterArduinoRollNeckIsconnected=RightPortIsConnected
		RollNeckArduino=eval(RollNeckArduino)
		
	except:
		errorSpokenFunc('BAdrduinoChoosen',', Roll Neck')
		isRollNeckActivated=0
		pass	
	
	if masterArduinoRollNeckIsconnected:
		talkEvent(lang_startingRollNeck)
		rollneck = Runtime.create("rollneck","Servo")
				
		rollneck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rollneck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rollneck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rollneck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rollneck')) 
		rollneck.setMaxVelocity(RollNeckMaxVelocity)
		rollneck.setRest(RollNeckRestPosition)
		
	
		if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rollneck'):rollneck.setInverted(True)
			
		rollneck = Runtime.start("rollneck","Servo")
		rollneck.attach(RollNeckArduino, RollNeckPin, RollNeckRestPosition, 100)
		rollneck.enableAutoAttach(1)
		rollneck.enableAutoDetach(0)
		rollneck.rest()
		
	else:
		#we force parameter if arduino is off
		isRollNeckActivated=0
		
#todo set inverted
