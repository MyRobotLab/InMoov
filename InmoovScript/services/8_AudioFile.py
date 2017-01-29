# ##############################################################################
# 								AUDIOFILE SERVICE
# ##############################################################################
# http://myrobotlab.org/service/audiofile

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

AudioPlayer = Runtime.createAndStart("AudioPlayer", "AudioFile")

python.subscribe(AudioPlayer.getName(),"publishAudioStart")
python.subscribe(AudioPlayer.getName(),"publishAudioEnd")

def onAudioStart(data):
	if AudioSignalProcessing and MouthControlActivated:
		head.jaw.attach()

def onAudioEnd(data):
	if AudioSignalProcessing and MouthControlActivated:
		head.jaw.detach()