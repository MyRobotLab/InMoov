# ##############################################################################
#            *** INMOOV LIFE ***
# ##############################################################################



  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  

#read current skeleton part config
inmoovLifeConfigFile=RuningFolder+'config/InMoovLife'

###############################################################################
#                 webgui sync
getInmoovFrParameter('inmoovlife',inmoovLifeConfigFile+'.config')
###############################################################################

CheckFileExist(inmoovLifeConfigFile)
inmoovLifeConfig = ConfigParser.ConfigParser()
inmoovLifeConfig.read(inmoovLifeConfigFile+'.config')

HealthCheckActivated=inmoovLifeConfig.getboolean('HEALTHCHECK', 'Activated')
HealthCheckTimerValue=inmoovLifeConfig.getint('HEALTHCHECK', 'TimerValue')

i01.RobotCanMoveHeadRandom=inmoovLifeConfig.getboolean('MOVEHEADRANDOM', 'RobotCanMoveHeadWhileSpeaking')
  
