# ##############################################################################
#						*** PIR SENSOR ***
# ##############################################################################




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


#analog pin listener
def publishPinPir(pins):
	global pirTimerStarted
	for pin in range(0, len(pins)):
		if pins[pin].value>0:
			pirTimerStarted=0
			pirTimer.stopClock()
			pirTimer.startClock()
		

if isPirActivated:
	try:
		PirControlerArduino=eval(PirArduino)
		talkEvent(lang_startingPir)
				
	except:
		errorSpokenFunc('BAdrduinoChoosen','pir')
		isPirActivated=0
		pass
		
#pir timer to avoid human detection notification every seconds...
global pirTimerStarted
pirTimerStarted=0

def pirTimerRoutine(timedata):

	global RobotPirHasDetectedHuman
	global pirTimerStarted
		
	if not RobotPirHasDetectedHuman:
		if PlayCurstomSoundIfDetection:AudioPlayer.playFile(RuningFolder+'/system/sounds/Notifications/'+random.choice(os.listdir(RuningFolder+'/system/sounds/Notifications')), False)
	RobotPirHasDetectedHuman=1
	if pirTimerStarted:
		RobotPirHasDetectedHuman=0
		pirTimer.stopClock()
	
	pirTimerStarted=1
	
	
			
if isPirActivated:
	pirTimer = Runtime.createAndStart("pirTimer","Clock")
	pirTimer.addListener("pulse", python.name, "pirTimerRoutine")
	pirTimer.setInterval(HumanPresenceTimeout)
	PirControlerArduino.addListener("publishPinArray","python","publishPinPir")
	PirControlerArduino.enablePin(PirPin,1)

		
