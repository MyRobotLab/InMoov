# ##############################################################################
# 								TIMERS ACTION
# ##############################################################################

###############################################################################
# Timer function to autostart webkit microphone every 10seconds
# only if robot not actualy speaking
###############################################################################
HealthCheck = Runtime.start("HealthCheck","Clock")
HealthCheck.setInterval(60000)

def HealthCheck_def(timedata):
	
	if RobotIsErrorMode==1:
		if error_red:
			PlayNeopixelAnimation("Flash Random", 255, 0, 0, 5)
	

HealthCheck.addListener("pulse", python.name, "HealthCheck_def")		
HealthCheck.startClock()

