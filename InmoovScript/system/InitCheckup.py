# ##############################################################################
# 								INITIAL CHECKUP
# ##############################################################################

#we import libraries
execfile(RuningFolder+'system/Import_Libraries.py')

#we load services python side from services folder
#I have some strange no blocking event with LoadGesture so use classic execfile
for filename in os.listdir(RuningFolder+'services'):
     execfile(RuningFolder+'services/'+filename)

#we include some error control
execfile(RuningFolder+'system/Errors.py')

i01.startMouth()
i01.startEar()
ear = i01.ear
mouth=i01.mouth

#set language	
if MyLanguage!="en":
	try:
		mouth.setLanguage(MyLanguage)
		
		i01.ear.setLanguage(MyLanguage)
	except:
		errorSpokenFunc('MyLanguage')
		pass


#check and update marytts voices	
if MyvoiceTTS=="MarySpeech":
	if not CheckMaryTTSVoice(voiceType):
		mouth.installComponentsAcceptLicense(voiceType)
		errorSpokenFunc('VoiceDownloaded')
		sleep(3)
		runtime.exit()
	
try:
	mouth.setVoice(voiceType)
except:
	errorSpokenFunc('voiceType')
	pass
	

# We do a checkup of arduinos and mrlcomm
if ScriptType=="FingerStarter":
	right = Runtime.createAndStart("i01.right", "Arduino")
	RightPortIsConnected=right.connect(MyRightPort)
	RightPortIsConnected=right.isConnected()
		
	if not RightPortIsConnected:
		errorSpokenFunc('RightPortIsConnected')
		
print right.getBoardInfo()


