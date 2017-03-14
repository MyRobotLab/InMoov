# ##############################################################################
#						*** PIR SENSOR ***
# ##############################################################################

# exemple after 5 minutes of inactivity we call the function sleepModeSleep()
# and if human is detected and if the robot sleeping we call sleepModeWakeUp()


# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=inspect.getfile(inspect.currentframe()).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isPirActivated=0

isPirActivated=ThisServicePartConfig.getboolean('MAIN', 'isPirActivated') 
PirPin=ThisServicePartConfig.getint('MAIN', 'PirPin') 
PirArduino=ThisServicePartConfig.get('MAIN', 'PirControlerArduino')
HumanPresenceTimeout=ThisServicePartConfig.getint('TWEAK', 'HumanPresenceTimeout')
PlayCurstomSoundIfDetection=ThisServicePartConfig.getboolean('MAIN', 'PlayCurstomSoundIfDetection')

# ##############################################################################
# 								SERVICE START
# ##############################################################################
#pir timer to avoid human detection notification every seconds...
global pirTimerStarted
pirTimerStarted=0
global SleepTimerAction
SleepTimerAction=""

#analog pin listener read the pir
def publishPinPir(pins):
	

	for pin in range(0, len(pins)):
		
		#human detected
		if pins[pin].value>0:
			if not RobotIsSleeping and RobotIsStarted:
				humanDetected()
			
			#wakeup action
			if RobotIsSleeping:
				PirControlerArduino.disablePin(PirPin)
				sleepModeWakeUp()


if isPirActivated:
	try:
		PirControlerArduino=eval(PirArduino)
		talkEvent(lang_startingPir)
				
	except:
		errorSpokenFunc('BAdrduinoChoosen','pir')
		isPirActivated=0
		pass