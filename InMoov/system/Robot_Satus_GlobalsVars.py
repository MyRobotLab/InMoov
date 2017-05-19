  
# ##############################################################################
#                 ROBOT STATUS
# ##############################################################################

  
# we try here to give explicit names of vars
# you can read them in your script
# DONT CHANGE VARS HERE THEY ARE DYNAMICAL , IT IS A DECLARATION PART

global RobotIsStarted
RobotIsStarted=0
global RobotIsErrorMode
RobotIsErrorMode=0
global RobotCanMoveBodyRamdom
RobotCanMoveBodyRamdom=0
global RobotIsSleeping
RobotIsSleeping=0
global RobotneedUpdate
RobotneedUpdate=0
global batterieLevel
batterieLevel=100
global iHaveInmoovFrKey
iHaveInmoovFrKey=0

#system values
#used by mouthcontrol audio signal processing
global AudioInputValues
AudioInputValues=[]
global MouthControlActivated
MouthControlActivated=0
global AudioSignalProcessing
AudioSignalProcessing=0
