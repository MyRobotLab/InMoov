# ##############################################################################
#                 CONFIGPARSER FILE
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
  
if Language=="fr":Language="fr-FR"
if Language=="en":Language="en-US"
if Language=="es":Language="es-ES"
if Language=="de":Language="de-DE"
if Language=="nl":Language="nl-NL"
if Language=="ru":Language="ru-RU"
if Language=="in":Language="hi-IN"
if Language=="it":Language="it-IT"
if Language=="fi":Language="fi-FI"
if Language=="pt":Language="pt-PT"

languageError=False
if not i01.setLanguage(Language):
  languageError=True
  i01.setLanguage("en-US")

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
