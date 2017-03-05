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


#analog pin listener read the pir
def publishPinPir(pins):
	global pirTimerStarted
	for pin in range(0, len(pins)):
		if pins[pin].value>0:
			if RobotIsStarted:
				print "pir event"
				pirTimerStarted=0
				pirTimer.stopClock()
				sleep(0.1)
				pirTimer.startClock()
			
			
		
#pir timer to avoid human detection notification every seconds...
global pirTimerStarted
pirTimerStarted=0
def pirTimerRoutine(timedata):
	global pirTimerStarted

	if RobotIsSleeping:
		PirControlerArduino.disablePin(PirPin)
		#wakup function to call
		sleepModeWakeUp()
		pirTimer.stopClock()
	
	if pirTimerStarted and not RobotIsSleeping:
		PirControlerArduino.disablePin(PirPin)
		#sleep function to call
		sleepModeSleep()
		pirTimer.stopClock()
	pirTimerStarted=1
	

#pir starting	
if isPirActivated:

	try:
		PirControlerArduino=eval(PirArduino)
		talkEvent(lang_startingPir)
				
	except:
		errorSpokenFunc('BAdrduinoChoosen','pir')
		isPirActivated=0
		pass

	pirTimer = Runtime.createAndStart("pirTimer","Clock")
	pirTimer.addListener("pulse", python.name, "pirTimerRoutine")
	pirTimer.setInterval(HumanPresenceTimeout)
	PirControlerArduino.addListener("publishPinArray","python","publishPinPir")
	PirControlerArduino.enablePin(PirPin,1)
	
	
