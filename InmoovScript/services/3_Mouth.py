# ##############################################################################
# 								MOUTH SERVICE FILE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

#read config
MyvoiceTTS=BasicConfig.get('TTS', 'MyvoiceTTS')
MyLanguage=BasicConfig.get('TTS', 'MyLanguage')
MyvoiceType=BasicConfig.get('TTS', 'MyvoiceType')

#subconsciousMouth is an always worky english voice used to diagnostic
subconsciousMouth = Runtime.createAndStart("subconsciousMouth", "MarySpeech")
subconsciousMouth.setVoice("cmu-slt-hsmm")

i01.mouth = Runtime.createAndStart("i01.mouth", MyvoiceTTS)
mouth=i01.mouth

python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

#functions to call about robot speak
def talk(data):
	if data:
		mouth.speak(unicode(data,'utf-8'))
		
def talkBlocking(data):
	if data:
		mouth.speakBlocking(unicode(data,'utf-8'))

#stop autolisten
def onEndSpeaking(text):
	global RobotIsActualySpeaking
	RobotIsActualySpeaking=0
	ear.resumeListening()
		
	
def onStartSpeaking(text):
	global RobotIsActualySpeaking
	RobotIsActualySpeaking=1
	ear.pauseListening()
		
MyLanguage=MyLanguage.lower()


# ##############################################################################
# MOUTH RELATED FUNCTIONS
# ##############################################################################

#to know what is marytts version
def getMaryttsVersion():
	try:
		versionMary=glob.glob(os.getcwd().replace("\\", "/")+'/libraries/jar/marytts-common-*.jar')[0].replace('.jar','').replace(os.getcwd().replace("\\", "/")+'/libraries/jar\marytts-common-','')
	except:
		versionMary=0
		pass
	return versionMary
	
#to check if marytts voice exist
def CheckMaryTTSVoice(voiceCheck):
	return os.access(os.getcwd().replace("\\", "/")+'/libraries/jar/voice-'+voiceCheck+'-'+getMaryttsVersion()+'.jar', os.R_OK)

#mouth functions
def setRobotLanguage():	
	if MyLanguage!="en":
		try:
			mouth.setLanguage(MyLanguage)
			i01.ear.setLanguage(MyLanguage)
		except:
			errorSpokenFunc('MyLanguage')
			pass
			
def checkAndDownloadVoice():				
	if MyvoiceTTS=="MarySpeech":
		if not CheckMaryTTSVoice(MyvoiceType):
			mouth.installComponentsAcceptLicense(MyvoiceType)
			errorSpokenFunc('VoiceDownloaded')
			sleep(3)
			runtime.exit()
		
def setCustomVoice():		
	try:
		mouth.setVoice(MyvoiceType)
	except:
		errorSpokenFunc('MyvoiceType')
		pass