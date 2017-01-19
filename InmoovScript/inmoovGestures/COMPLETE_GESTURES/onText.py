#We intercept what the robot is listen to change some values
#here we replace ' by space because AIML doesn't like '
def onText(text):
	global Voice
	#inmoovFrench.getResponse(text.replace("'", " "))