# ##############################################################################
#						*** HEAD ***
# ##############################################################################



  
# ##############################################################################
# 							PERSONNAL PARAMETERS
# ##############################################################################  
isHeadActivated=0  
#read current skeleton part config
ThisSkeletonPart=inspect.getfile(inspect.currentframe()).replace('.py','')
try:
	CheckFileExist(ThisSkeletonPart)
	ThisSkeletonPartConfig = ConfigParser.ConfigParser()
	ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

	isHeadActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isHeadActivated') 
	autoDetach=ThisSkeletonPartConfig.getboolean('MAIN', 'autoDetach')
	MouthControlActivated=ThisSkeletonPartConfig.getboolean('MOUTHCONTROL', 'MouthControlActivated')
	AudioSignalProcessing=ThisSkeletonPartConfig.getboolean('AUDIOSIGNALPROCESSING', 'AudioSignalProcessing')
	AnalogPinFromSoundCard=ThisSkeletonPartConfig.getint('AUDIOSIGNALPROCESSING', 'AnalogPin')
	HowManyPollsBySecond=ThisSkeletonPartConfig.getint('AUDIOSIGNALPROCESSING', 'HowManyPollsBySecond')
	jawMIN=ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw')
	jawMAX=ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw')
except:
	isHeadActivated=0
	errorSpokenFunc('ConfigParserProblem','head.config')
	pass
    
  
  
  
# ##############################################################################
# 								SERVO FUNCTIONS
# ##############################################################################

if isHeadActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full"):
	if LeftPortIsConnected:
		talkEvent(lang_startingHead)
		head = Runtime.create("i01.head","InMoovHead")
		#map		
		head.jaw.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'jaw'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw')) 
		head.eyeX.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyeX'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyeX')) 
		head.eyeY.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyeY'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyeY')) 
		head.neck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'neck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'neck')) 
		head.rothead.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rothead'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rothead'))
		
		#velocity
		#head.jaw.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'jaw'))
		#head.eyeX.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'eyeX'))
		#head.eyeY.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'eyeY'))
		head.neck.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'neck'))
		head.rothead.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'rothead'))
		
		#maxvelocity
		head.neck.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'neck'))
		head.rothead.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rothead'))
		
		#rest
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
				
		#head.jaw.enableAutoAttach(1)
		#head.jaw.autoDetach()
		
		if autoDetach:
			
			head.eyeX.enableAutoAttach(1)
			head.eyeY.enableAutoAttach(1)
			head.neck.enableAutoAttach(1)
			head.rothead.enableAutoAttach(1)
			
		head.detach()
		
		head.jaw.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'jaw'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'jaw'))
		head.eyeX.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'eyeX'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'eyeX'))
		head.eyeY.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'eyeY'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'eyeY'))
		head.neck.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'neck'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'neck'))
		head.rothead.attach(left,ThisSkeletonPartConfig.getint('SERVO_PIN', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MAP_REST', 'rothead'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rothead'))
		head.attach()
		head.jaw.setSpeed(1.0)
		
# ##############################################################################
# 								Software mouth control
# ##############################################################################		
		
		if MouthControlActivated and AudioSignalProcessing==False:
			MouthControl = Runtime.createAndStart("i01.mouthControl","MouthControl")
			#i01.startMouthControl(MyLeftPort)
			print "software mouthcontrol activation"
			MouthControl.setArduino(left)
			MouthControl.setJaw(head.jaw)
			MouthControl.startService()
			MouthControl.setmouth(ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw'))
		
# ##############################################################################
# 								mouth control based on audio signal processing
# ##############################################################################	
		
		#please set aref
		if AudioSignalProcessing:
			left.addListener("publishPinArray","python","publishPinLeft")
			AudioSignalProcessing=False
			MouthControlActivated=False
			AudioSignalProcessingCalibration=1
			left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
			talkBlocking(lang_MouthSyncronisation)
			
			
			AudioSignalProcessingCalibration=0
			maxAudioValue=maxAverage(AudioInputValues,10)
			AudioInputValues=[]
			AudioSignalProcessingCalibration=1
			sleep(3)
			AudioSignalProcessingCalibration=0
			minAudioValue = (sum(AudioInputValues) / len(AudioInputValues)) + 20
			left.disablePin(AnalogPinFromSoundCard)
			result=0
			#arduino dit not detect analog value
			if minAudioValue>50:
				talkBlocking(lang_MouthSyncronisationBad+str(AnalogPinFromSoundCard))
				result=1
			#arduino detect a poor value
			if result==0 and (maxAudioValue-minAudioValue<=255):
				head.jaw.map(minAudioValue,maxAudioValue,jawMIN,jawMAX)
				AudioSignalProcessing=True
				talkBlocking(lang_MouthSyncronisationNotPerfect)
			#arduino detect a good value	
			if result==0 and (maxAudioValue-minAudioValue>255):
				head.jaw.map(minAudioValue,maxAudioValue,jawMIN,jawMAX)
				AudioSignalProcessing=True
				talkBlocking(lang_MouthSyncronisationOk)
				
			print maxAudioValue,minAudioValue
		
		
	else:
		#we force parameter if arduino is off
		isHeadActivated=0
		MouthControlActivated=0
		
else:
	MouthControlActivated=0
		
#todo set inverted
