# ##############################################################################
#                 CONFIGPARSER FILE
# ##############################################################################

# ##############################################################################
#                 webgui sync
getInmoovFrParameter('config',RuningFolder+'config/' + '_Inmoov.config')
# ##############################################################################


#shared parse function
def CheckFileExist(File):
  global RobotIsErrorMode
  if not os.path.isfile(File+'.config'):
    shutil.move(File+'.config.default',File+'.config')
    print "config file created : ",File+'.config'


CheckFileExist(RuningFolder+'config/' + '_InMoov')
LaunchSwingGui=True
   
BasicConfig = ConfigParser.ConfigParser(allow_no_value = True)
BasicConfig.read(RuningFolder+'config/' + '_InMoov.config')

# PARSE THE CONFIG FILE
ScriptType=BasicConfig.get('MAIN', 'ScriptType')

try:
  MyLanguage=BasicConfig.get('TTS', 'MyLanguage')
  Language=MyLanguage
except:
  pass
  
try:
  Language=BasicConfig.get('MAIN', 'Language')
except:
  pass

DEBUG=BasicConfig.getboolean('MAIN', 'debug')
IsMute=BasicConfig.getboolean('VOCAL', 'IsMute')
LoadingPicture=BasicConfig.getboolean('GENERAL', 'LoadingPicture')
StartupSound=BasicConfig.getboolean('GENERAL', 'StartupSound')
IuseLinux=BasicConfig.getboolean('GENERAL', 'IuseLinux')
LaunchSwingGui=BasicConfig.getboolean('GENERAL', 'LaunchSwingGui')
BetaVersion=BasicConfig.getboolean('GENERAL', 'BetaVersion')

#for noworky
log.info("_inmoov.config")
log.info("ScriptType : "+str(ScriptType))
log.info("Language : "+str(Language))