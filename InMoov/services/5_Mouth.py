# -- coding: utf-8 --
# ##############################################################################
#                 MOUTH SERVICE FILE
# ##############################################################################


# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

global VoiceError
VoiceError=0
try:
  #subconsciousMouth is an always worky english voice used to diagnostic
  #inmoov mouth service
  i01.mouth = Runtime.createAndStart("i01.mouth", MyvoiceTTS)
  mouth=i01.mouth
  #mouth.speak(",")
  
except:
  mouth=subconsciousMouth
  errorSpokenFunc('MyvoiceType')
  VoiceError=1
  pass


#vocal startup globalized so :
i01.setMute(1)

python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################
global lastValue
lastValue=0
#analog pin listener use 
def publishMouthcontrolPinLeft(pins):
  global AudioInputValues
  global AudioInputRawValue

  for pin in range(0, len(pins)):
    
    #mouth control listener
    if isHeadActivated:
      if AudioSignalProcessingCalibration:AudioInputValues.append(pins[pin].value)
        
      if AudioSignalProcessing:
        if pins[pin].value>minAudioValue:
          head.jaw.setVelocity(random.uniform(80,120))
          if not head.jaw.isMoving():head.jaw.moveTo(int(pins[pin].value))
    
          



#functions to call about robot speak
def talk(data):
  if data:
    if data[0:2]=="l ":data=data.replace("l ", "l'")
    if MyvoiceTTS!="VoiceRss":data=unicode(data,'utf-8')
    mouth.speak(data)
    
def talkBlocking(data):
  if data:
    if data[0:2]=="l ":data=data.replace("l ", "l'")
    if MyvoiceTTS!="VoiceRss":data=unicode(data,'utf-8')
    mouth.speakBlocking(data)
    
def talkEvent(data):
  if IsMute==0:
    if MyvoiceTTS!="VoiceRss":data=unicode(data,'utf-8')
    subconsciousMouth.speakBlocking(data)

#stop autolisten
def onEndSpeaking(text):
  global RobotIsActualySpeaking
  global RobotCanMoveHeadWhileSpeaking
  RobotIsActualySpeaking=0
  if RobotIsStarted==1:
    
    MoveHeadTimer.stopClock()
    if flash_when_speak:
      StopNeopixelAnimation()
    
    RobotCanMoveHeadWhileSpeaking=1
  if AudioSignalProcessing:
    try:
      left.disablePin(AnalogPinFromSoundCard)
      head.jaw.setVelocity(20)
      head.jaw.moveTo(0)
      #head.jaw.setVelocity(200)
      #head.jaw.moveTo(0)
    except:
      print "onEndSpeaking error"
      pass
  
  
  
def onStartSpeaking(text):
  
  global RobotIsActualySpeaking
  RobotIsActualySpeaking=1
  
  if AudioSignalProcessing:
    try:
      
      left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
      
    except:
      print "onStartSpeaking error"
      pass
  if RobotIsStarted:
    MoveHeadTimer.startClock()
    if flash_when_speak:    
      PlayNeopixelAnimation("Flash Random", 255, 255, 255, 1)
    



# ##############################################################################
# MOUTH RELATED FUNCTIONS
# ##############################################################################

#to know what is marytts version
def getMaryttsVersion():
  try:
    versionMary=glob.glob(os.getcwd().replace("\\", "/")+'/libraries/jar/marytts-common-*.jar')[0].replace('.jar','').replace(os.getcwd().replace("\\", "/")+'/libraries/jar\marytts-common-','')
  except:
    versionMary=0
    pass
  return versionMary
  
#to check if marytts voice exist
def CheckMaryTTSVoice(voiceCheck):
  return os.access(os.getcwd().replace("\\", "/")+'/libraries/jar/voice-'+voiceCheck+'-'+getMaryttsVersion()+'.jar', os.R_OK)

#mouth functions
def setRobotLanguage():
  global LanguageError
  LanguageError=0
  tmplanguage=MyLanguage
  if MyvoiceTTS=="VoiceRss" or MyvoiceTTS=="Polly":
    if tmplanguage=="fr":tmplanguage="fr-fr"
    if tmplanguage=="en":tmplanguage="en-us"
    if tmplanguage=="es":tmplanguage="es-es"
    if tmplanguage=="de":tmplanguage="de-de"
    if tmplanguage=="nl":tmplanguage="nl-nl"
  
  try:
    if MyvoiceTTS=="VoiceRss":i01.mouth.setKey(VoiceRssApi)
  except:
    pass
    
  try:  
    if MyvoiceTTS=="Polly":i01.mouth.setKey(awsaccesskeyid,awssecretkey)
  except:
    pass

  
  try:
    if MyvoiceTTS=="MarySpeech" and MyLanguage=="en":
      print ""
    else:
      mouth.setLanguage(tmplanguage)
    if EarEngine!="Sphinx":
      i01.ear.setLanguage(MyLanguage)
  except:
    errorSpokenFunc('MyLanguage')
    LanguageError=1
    pass
  
      
def checkAndDownloadVoice():        
  if MyvoiceTTS=="MarySpeech":
    if not CheckMaryTTSVoice(MyvoiceType):
      mouth.installComponentsAcceptLicense(MyvoiceType)
      if os.access(os.getcwd().replace("\\", "/")+'/libraries/jar/voice-'+MyvoiceType+'-'+getMaryttsVersion()+'.jar', os.R_OK):
        errorSpokenFunc('VoiceDownloaded')
        sleep(4)
        runtime.exit()
      else:
        errorSpokenFunc('I_cannot_download_this_mary_T_T_S_voice',MyvoiceType)
        
    
def setCustomVoice():  
  global VoiceError
  VoiceError=0
  try:
    mouth.setVoice(unicode(MyvoiceType,'utf-8'))
  except:
    errorSpokenFunc('MyvoiceType')
    VoiceError=1
    pass
    
#we start raw Inmoov ear and mouth service
i01.startMouth()
#set user language

setRobotLanguage()

#check and update marytts voices  
#no worky on linux
if not IuseLinux:
  checkAndDownloadVoice()
#set CustomVoice
setCustomVoice()
#set english subconsious mouth to user globalised mouth now ( only if we found a language pack )


try:
  mouth.speak(",")
except:
  errorSpokenFunc('lang_VoiceRssNoWorky')
  VoiceError=1
  mouth=subconsciousMouth
  pass

if languagePackLoaded==1 and LanguageError==0 and VoiceError==0:
  subconsciousMouth=mouth
if languagePackLoaded==0:
  errorSpokenFunc('BadLanguagePack')


talkEvent(lang_whatIsThisLanguage)
talkEvent(lang_startingEar+", "+EarEngine)