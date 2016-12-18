# ##############################################################################
# MOUTH TWEAKS FILE
# ##############################################################################

#subconsciousMouth is an always worky english voice used to diagnostic
subconsciousMouth = Runtime.createAndStart("subconsciousMouth", "MarySpeech")
subconsciousMouth.setVoice("cmu-slt-hsmm")

i01.mouth = Runtime.createAndStart("i01.mouth", MyvoiceTTS)


#function to call about robot speak
def talk(data):
	if data:
		i01.mouth.speak(unicode(data,'utf-8'))
		
def talkBlocking(data):
	if data:
		i01.mouth.speakBlocking(unicode(data,'utf-8'))
		
MyLanguage=MyLanguage.lower()


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