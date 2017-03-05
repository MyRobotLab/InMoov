# ##############################################################################
# 								AUDIOFILE SERVICE
# ##############################################################################
# http://myrobotlab.org/service/audiofile

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

#startup sound
AudioPlayer = Runtime.createAndStart("AudioPlayer", "AudioFile")

def onAudioStart(data):
	if AudioSignalProcessing and isHeadActivated:
		print "onaudiostart"
		try:
			head.attach()
			head.jaw.moveTo(180)
			left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
		except:
			print "onAudioStart error"
			pass

def onAudioEnd(data):
	if AudioSignalProcessing and isHeadActivated:
		try:
			left.disablePin(AnalogPinFromSoundCard)
			#head.jaw.detach()
		except:
			print "onAudioEnd error"
			pass
			
def AudioPlay(file):
	AudioPlayer.playFile(file,False)
			


python.subscribe(AudioPlayer.getName(),"publishAudioStart")
python.subscribe(AudioPlayer.getName(),"publishAudioEnd")
if StartupSound:AudioPlayer.playFile(RuningFolder+'/system/sounds/startupsound.mp3', False)