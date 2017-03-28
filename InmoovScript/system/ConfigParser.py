# ##############################################################################
#                 CONFIGPARSER FILE
# ##############################################################################

# ##############################################################################
#                 webgui sync
getInmoovFrParameter('config',RuningFolder+"Inmoov.config")
# ##############################################################################


#shared parse function
def CheckFileExist(File):
  global RobotIsErrorMode
  if not os.path.isfile(File+'.config'):
    shutil.move(File+'.config.default',File+'.config')
    print "config file created : ",File+'.config'

  
CheckFileExist(RuningFolder + 'Inmoov')
LaunchSwingGui=True


   
BasicConfig = ConfigParser.ConfigParser(allow_no_value = True)
BasicConfig.read(RuningFolder+'Inmoov.config')

#file patch
configNeedUpdate=0
try:
    VoiceRssApi = BasicConfig.get('TTS', 'VoiceRssApi')
except:
  BasicConfig.set('TTS', 'VoiceRssApi', 'xxx')
  configNeedUpdate=1
  pass
  
try:
    VoiceRssApi = BasicConfig.get('GENERAL', 'BetaVersion')
except:
  BasicConfig.set('GENERAL', 'BetaVersion', 1)
  configNeedUpdate=1
  pass
  
  
try:
    if BasicConfig.get('VOCAL', 'EarInterpretEngine')!='':
      BasicConfig.remove_option('VOCAL', 'EarInterpretEngine')
      configNeedUpdate=1
except:
  pass  
  
if configNeedUpdate:
  with open(RuningFolder+'Inmoov.config', 'wb') as f:
    BasicConfig.write(f)

try:
  # PARSE THE CONFIG FILE
  ScriptType=BasicConfig.get('MAIN', 'ScriptType')
  MyRightPort=BasicConfig.get('ARDUINO', 'MyRightPort')
  MyLeftPort=BasicConfig.get('ARDUINO', 'MyLeftPort')
  ForceArduinoIsConnected=BasicConfig.getboolean('ARDUINO', 'ForceArduinoIsConnected')
  #read personnal config
  MyvoiceTTS=BasicConfig.get('TTS', 'MyvoiceTTS')
  MyLanguage=BasicConfig.get('TTS', 'MyLanguage')
  VoiceRssApi=BasicConfig.get('TTS', 'VoiceRssApi')
  MyvoiceType=BasicConfig.get('TTS', 'MyvoiceType')
  if MyvoiceType[0]=="[":
    MyvoiceType=MyvoiceType.split(']', 1 )[1]
  DEBUG=BasicConfig.getboolean('MAIN', 'debug')
  IsMute=BasicConfig.getboolean('VOCAL', 'IsMute')
  EarEngine=BasicConfig.get('VOCAL', 'EarEngine')
  LoadingPicture=BasicConfig.getboolean('GENERAL', 'LoadingPicture')
  StartupSound=BasicConfig.getboolean('GENERAL', 'StartupSound')
  IuseLinux=BasicConfig.getboolean('GENERAL', 'IuseLinux')
  LaunchSwingGui=BasicConfig.getboolean('GENERAL', 'LaunchSwingGui')
  BetaVersion=BasicConfig.getboolean('GENERAL', 'BetaVersion')


except:
  
  print 'ConfigParserProblem'
  RobotIsErrorMode=1
  pass  
