# ##############################################################################
#						*** NEOPIXEL SERVICE ***
# ##############################################################################


 
  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current skeleton part config
ThisServicePart=inspect.getfile(inspect.currentframe()).replace('.py','')
CheckConfigFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

isNeopixelActivated=ThisServicePartConfig.getboolean('MAIN', 'isNeopixelActivated') 

pin=ThisServicePartConfig.getint('NEOPIXEL', 'pin') 
numberOfPixel=ThisServicePartConfig.getint('NEOPIXEL', 'numberOfPixel')


  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isNeopixelActivated==1:
	
	neopixelArduino = Runtime.createAndStart("neopixelArduino", "Arduino")
	neopixelArduinoIsConnected=CheckArduinos(eval(ThisServicePartConfig.get('MAIN', 'NeopixelMaster')),ThisServicePartConfig.get('MAIN', 'NeopixelMasterPort') )
	

		#Starting NeoPixel Service
	neopixel = Runtime.createAndStart("neopixel","NeoPixel")

	#neopixel.attach(arduino, pin, number of pixel)
	neopixel.attach(neopixelArduino, pin, numberOfPixel)

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
	#starting a animation
	#neopixel.setAnimation("Animation Name", red, green, blue, speed)
	neopixel.setAnimation("Theater Chase", 255, 0, 0, 1) #running Theater Chase with color red at full speed

	sleep(10)
	neopixel.animationStop()

	#run an animation with python script
	#turn off all the pixels
	for pixel in range (1,neopixel.numPixel + 1):
	  neopixel.setPixel(pixel, 0, 0, 0)  #setPixel(pixel, red, green, blue)
	neopixel.writeMatrix() #send the pixel data to the Neopixel hardware 
	for loop in range(0,10): #do 10 loop
	  for pixel in range(1, neopixel.numPixel +1):
		neopixel.setPixel(pixel, 0, 255, 0) #set the pixel to red
		neopixel.writeMatrix()
		sleep(0.03) #give a bit of delay before next step
		neopixel.setPixel(pixel, 0, 0, 0) #turn off the pixel
	neopixel.writeMatrix()