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

#file patch
configNeedUpdate=0
try:
  VoiceRssApi = BasicConfig.get('TTS', 'VoiceRssApi')
except:
  BasicConfig.set('TTS', 'VoiceRssApi', 'xxx')
  configNeedUpdate=1
  pass
  
try:
  IndianTtsApi = BasicConfig.get('TTS', 'IndianTtsApi')
except:
  BasicConfig.set('TTS', 'IndianTtsApi', '')
  BasicConfig.set('TTS', 'IndianTtsUserId', '')
  configNeedUpdate=1
  pass

  
if configNeedUpdate:
  with open(RuningFolder+'config/' + '_InMoov.config', 'wb') as f:
    BasicConfig.write(f)


# PARSE THE CONFIG FILE
ScriptType=BasicConfig.get('MAIN', 'ScriptType')
#read personnal config
MyvoiceTTS=BasicConfig.get('TTS', 'MyvoiceTTS')
if MyvoiceTTS=="MicrosoftLocalTTS":MyvoiceTTS="LocalSpeech"
MyLanguage=BasicConfig.get('TTS', 'MyLanguage')
VoiceRssApi=BasicConfig.get('TTS', 'VoiceRssApi')
MyvoiceType=BasicConfig.get('TTS', 'MyvoiceType')
awsaccesskeyid=BasicConfig.get('TTS', 'awsaccesskeyid')
awssecretkey=BasicConfig.get('TTS', 'awssecretkey')
IndianTtsApi=BasicConfig.get('TTS', 'IndianTtsApi')
IndianTtsUserId=BasicConfig.get('TTS', 'IndianTtsUserId')
if MyvoiceType[0]=="[":
  MyvoiceType=MyvoiceType.split(']', 1 )[1]
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
log.info("MyvoiceTTS : "+str(MyvoiceTTS))
log.info("MyLanguage : "+str(MyLanguage))
log.info("MyvoiceType : "+str(MyvoiceType))
log.info("ScriptType : "+str(ScriptType))
log.info("MyvoiceTTS : "+str(MyvoiceTTS))
log.info("MyLanguage : "+str(MyLanguage))
log.info("MyvoiceType : "+str(MyvoiceType))