# ##############################################################################
# MOUTH TWEAKS FILE
# ##############################################################################

def talk(data):
	if data:
		mouth.speak(unicode(data,'utf-8'))
		
def talkBlocking(data):
	if data:
		mouth.speakBlocking(unicode(data,'utf-8'))