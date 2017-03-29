# ##############################################################################
#            *** INMOOV LIFE ***
# ##############################################################################



  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  

#read current skeleton part config
inmoovLifeConfigFile=inspect.getfile(inspect.currentframe()).replace('.py','')

# ##############################################################################
#                 webgui sync
getInmoovFrParameter('inmoovlife',ThisServicePart+'.config')
# ##############################################################################

CheckFileExist(inmoovLifeConfigFile)
inmoovLifeConfig = ConfigParser.ConfigParser()
inmoovLifeConfig.read(inmoovLifeConfigFile+'.config')

AutolistenActivated=inmoovLifeConfig.getboolean('AUTOLISTEN', 'Activated') 
AutolistenTimerValue=inmoovLifeConfig.getint('AUTOLISTEN', 'TimerValue') 
HealthCheckActivated=inmoovLifeConfig.getboolean('HEALTHCHECK', 'Activated')
HealthCheckTimerValue=inmoovLifeConfig.getint('HEALTHCHECK', 'TimerValue')
global RobotCanMoveHeadWhileSpeaking
RobotCanMoveHeadWhileSpeaking=inmoovLifeConfig.getboolean('MOVEHEADRANDOM', 'RobotCanMoveHeadWhileSpeaking')
  
