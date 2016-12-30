# ##############################################################################
#						*** MRL SERVICE - NEOPIXEL  ***
# ##############################################################################

	#TODO ADD PIXEL MATRIX
	
	#Animations;
	#"Color Wipe"
	#"Larson Scanner"
	#"Theater Chase"
	#"Theater Chase Rainbow"
	#"Rainbow"
	#"Rainbow Cycle"
	#"Flash Random"
	#"Ironman"

	#speed: 1-65535   1=full speed, 2=2x slower than 1, 10=10x slower than 1
	#starting a animation :
##	neopixel.setAnimation("Animation Name", red, green, blue, speed)
##	optional : PlayNeopixelAnimation("Animation Name", red, green, blue, speed, duration) > thread animation timeout

# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=inspect.getfile(inspect.currentframe()).replace('.py','')
CheckConfigFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
isNeopixelActivated=0
isNeopixelActivated=ThisServicePartConfig.getboolean('MAIN', 'isNeopixelActivated') 

pin=ThisServicePartConfig.getint('NEOPIXEL', 'pin') 
numberOfPixel=ThisServicePartConfig.getint('NEOPIXEL', 'numberOfPixel')
  
# ##############################################################################
# 								SERVICE START
# ##############################################################################

if isNeopixelActivated==1:
	neopixelArduino = Runtime.createAndStart("arduino2","Arduino")
	try:
		neopixelArduinoIsConnected=CheckArduinos(neopixelArduino,ThisServicePartConfig.get('MAIN', 'NeopixelMasterPort'),eval(ThisServicePartConfig.get('MAIN', 'NeopixelMaster')))
	except:
		errorSpokenFunc('BAdrduinoChoosen','Neo pixel')
		isNeopixelActivated=0
		neopixelArduinoIsConnected=0
		pass	
	
	
	sleep(1)

	neopixel = Runtime.createAndStart("neopixel","NeoPixel")
	if neopixelArduinoIsConnected==True:
		#Starting NeoPixel Service
		neopixel.attach(neopixelArduino, pin, numberOfPixel)
	else:
		isNeopixelActivated=0


	
def StopNeopixelAnimation():
	if isNeopixelActivated==1:
		neopixel.animationStop()
		neopixel.turnOff

def PlayNeopixelAnimation_Thread(Animation_Name,red=255,green=255,blue=255,speed=1,duration=0):
	processThread = threading.Thread(target=PlayNeopixelAnimation_NoThread, args=(Animation_Name,red,green,blue,speed,duration,))
	processThread.start()
	
def PlayNeopixelAnimation_NoThread(Animation_Name,red=255,green=255,blue=255,speed=1,duration=0):			
	if isNeopixelActivated==1:
		StopNeopixelAnimation()
		neopixel.turnOn
		neopixel.setAnimation(Animation_Name, red, green, blue, speed)
		if duration!=0:
			sleep(duration)
			StopNeopixelAnimation() 
			
PlayNeopixelAnimation_NoThread("Theater Chase", 0, 255, 0, 1) #running Theater Chase with color red at full speed
