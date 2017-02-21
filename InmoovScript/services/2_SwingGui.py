# ##############################################################################
# 								SWINGGUI SERVICE
# ##############################################################################
# 

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

if LaunchSwingGui:
	try:
		SwingGui=Runtime.createAndStart("SwingGui", "SwingGui")
		GUIService=Runtime.createAndStart("GUIService", "GUIService")
	except:
		pass