  
# ##############################################################################
# 								ROBOT STATUS
# ##############################################################################

	
# we try here to give explicit names of vars
# you can read them in your script
# DONT CHANGE VARS HERE THEY ARE DYNAMICAL , IT IS A DECLARATION PART

global RobotIsStarted
RobotIsStarted=0
global RobotIsActualySpeaking
RobotIsActualySpeaking=0
global RobotIsErrorMode
RobotIsErrorMode=0


#system values
#used by mouthcontrol audio signal processing
global AudioInputValues
AudioInputValues=[]
global MouthControlActivated
MouthControlActivated=0
global AudioSignalProcessing
AudioSignalProcessing=0