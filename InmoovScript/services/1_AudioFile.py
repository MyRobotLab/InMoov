# ##############################################################################
# 								AUDIOFILE SERVICE
# ##############################################################################
# http://myrobotlab.org/service/audiofile

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################


python.subscribe(AudioPlayer.getName(),"publishAudioStart")
python.subscribe(AudioPlayer.getName(),"publishAudioEnd")

def onAudioStart(data):
	if AudioSignalProcessing and isHeadActivated:
		head.jaw.attach()

def onAudioEnd(data):
	if AudioSignalProcessing and isHeadActivated:
		head.jaw.detach()