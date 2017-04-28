# ##############################################################################
#            *** INMOOV LIFE ***
# ##############################################################################



  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  

#read current skeleton part config
inmoovLifeConfigFile=inspect.getfile(inspect.currentframe()).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('inmoovlife',inmoovLifeConfigFile+'.config')
###############################################################################

CheckFileExist(inmoovLifeConfigFile)
inmoovLifeConfig = ConfigParser.ConfigParser()
inmoovLifeConfig.read(inmoovLifeConfigFile+'.config')

HealthCheckActivated=inmoovLifeConfig.getboolean('HEALTHCHECK', 'Activated')
HealthCheckTimerValue=inmoovLifeConfig.getint('HEALTHCHECK', 'TimerValue')
global RobotCanMoveHeadWhileSpeaking
RobotCanMoveHeadWhileSpeaking=inmoovLifeConfig.getboolean('MOVEHEADRANDOM', 'RobotCanMoveHeadWhileSpeaking')
  
