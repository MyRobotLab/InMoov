# -- coding: utf-8 --
# ##############################################################################
#                 MOUTH SERVICE FILE
# ##############################################################################


# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

Speechengine=ThisServicePartConfig.get('TTS', 'Speechengine')
VoiceName=unicode(ThisServicePartConfig.get('TTS', 'VoiceName'),'utf-8')
apiKey1=ThisServicePartConfig.get('API_KEY', 'apiKey1')
apiKey2=ThisServicePartConfig.get('API_KEY', 'apiKey2')

#for noworky
log.info("mouth.config")
log.info("Speechengine : "+str(Speechengine))
log.info("VoiceName : "+ VoiceName)
log.info("Language : "+str(Language))

#compatibility
MyvoiceTTS=Speechengine
MyvoiceType=VoiceName

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

global VoiceError
VoiceError=False

try:mouth=Runtime.start("i01.mouth", Speechengine)
except:pass

if not mouth:
  mouth=Runtime.start("i01.mouth", "MarySpeech")
  errorSpokenFunc('MyvoiceType')
  VoiceError=True

#vocal startup globalized so :
i01.setMute(True)

python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")

# ##############################################################################
# MRL SERVICE TWEAKS
# ##############################################################################

#analog pin listener use 
def publishMouthcontrolPinLeft(pins):
  global AudioInputValues
  global AudioInputRawValue

  for pin in range(0, len(pins)):
    #print pins[pin].value
    #mouth control listener
    if isHeadActivated:
      if AudioSignalProcessingCalibration:AudioInputValues.append(pins[pin].value)
        
      if AudioSignalProcessing:
        if pins[pin].value>minAudioValue:
          head.jaw.setVelocity(random.uniform(200,500))
          if not head.jaw.isMoving():head.jaw.moveTo(int(pins[pin].value))
    

#functions to call about robot speak
def talk(data):
  if data:
    data=unicode(data,'utf-8')
    if data[0:2].lower()=="l ":data=data.replace("l ", "l'")
    if data[0:2].lower()=="j ":data=data.replace("j ", "j'")
    if data[0:2].lower()=="c ":data=data.replace("c ", "c'")
    if data[0:2].lower()=="d ":data=data.replace("d ", "d'")
    data=data.lower().replace(" j ", " j'")
    data=data.lower().replace(" l ", " l'")
    data=data.lower().replace(" c ", " c'")
    data=data.lower().replace(" d ", " d'")
    data=data.lower().replace("it s", "it's")
    mouth.speak(data)
    
def talkBlocking(data):
  if data:
    data=unicode(data,'utf-8')
    if data[0:2].lower()=="l ":data=data.replace("l ", "l'")
    if data[0:2].lower()=="j ":data=data.replace("j ", "j'")
    if data[0:2].lower()=="c ":data=data.replace("c ", "c'")
    if data[0:2].lower()=="d ":data=data.replace("d ", "d'")
    data=data.lower().replace(" j ", " j'")
    data=data.lower().replace(" l ", " l'")
    data=data.lower().replace(" c ", " c'")
    data=data.lower().replace(" d ", " d'")
    data=data.lower().replace("it s", "it's")
    data=data.replace(" j ", " j'")
    data=data.replace(" l ", " l'")
    mouth.speakBlocking(data)
    
def talkEvent(data):
  if IsMute==0:
    data=unicode(data,'utf-8')
    subconsciousMouth.speakBlocking(data)

#stop autolisten
def onEndSpeaking(text):

  if i01.RobotIsStarted:
    
    if not MoveRandomTimer.isClockRunning:
      MoveHeadTimer.stopClock()
      MoveEyesTimer.stopClock()
    if flash_when_speak and isNeopixelActivated:i01.stopNeopixelAnimation()

  if AudioSignalProcessing:
    try:
      left.disablePin(AnalogPinFromSoundCard)
      head.jaw.setVelocity(100)
      head.jaw.moveTo(0)
      #head.jaw.setVelocity(200)
      #head.jaw.moveTo(0)
    except:
      print "onEndSpeaking error"
      pass
  
def onStartSpeaking(text):
  
  if AudioSignalProcessing:
    try:left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)      
    except:
      print "onStartSpeaking error"
      pass
  if i01.RobotIsStarted:

    if 'oui ' in text or 'yes ' in text or ' oui' in text or 'ja ' in text or text=="yes" or text=="kyllä":Yes()
    if 'non ' in text or 'no ' in text or 'nicht ' in text or 'neen ' in text or text=="no" or text=="ei":No()

    #force random move while speaking, to avoid conflict with random life gesture
    if random.randint(0,1)==1:
      i01.RobotCanMoveHeadRandom=True
      MoveHeadTimer.startClock()
    if random.randint(0,1)==1:
      i01.RobotCanMoveEyesRandom=True
      MoveEyesTimer.startClock()
    if flash_when_speak and isNeopixelActivated:i01.setNeopixelAnimation("Flash Random", 255, 255, 255, 1)
    
# ##############################################################################
# MOUTH RELATED FUNCTIONS
# ##############################################################################


#mouth functions
def setRobotLanguage():
  global LanguageError
  LanguageError=False
  
  try:
    if Speechengine=="VoiceRss":i01.mouth.setKey("VOICERSS_API_KEY",apiKey1)
  except:
    pass
    
  try:  
    if Speechengine=="Polly":i01.mouth.setKeys(apiKey1,apiKey2)
  except:
    pass
    
  try:  
    if Speechengine=="IndianTts":i01.mouth.setKeys(apiKey2,apiKey1)
  except:
    pass

  
  try:
    if EarEngine=="WebkitSpeechRecognition":i01.ear.setcurrentWebkitLanguage(Language)
    mouth.setLanguage(Language)
  except:
    errorSpokenFunc('Language')
    LanguageError=True
    pass
  
   
    
def setCustomVoice():  
  global VoiceError
  VoiceError=False
  try:
    mouth.setVoice(VoiceName)
  except:
    errorSpokenFunc('MyvoiceType')
    VoiceError=True
    pass
    
#we start raw Inmoov ear and mouth service
i01.startMouth()
#set user language

setRobotLanguage()

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
  
credentialsError=False
if Speechengine=="Polly" or Speechengine=="VoiceRss" or Speechengine=="IndianTts":credentialsError=mouth.credentialsError
if credentialsError:
  errorSpokenFunc('lang_VoiceRssNoWorky')
  VoiceError=1
  mouth=subconsciousMouth

if languagePackLoaded and not LanguageError and not VoiceError:
  subconsciousMouth=mouth
if not languagePackLoaded:
  errorSpokenFunc('BadLanguagePack')


talkEvent(lang_whatIsThisLanguage)
talkEvent(lang_startingEar+", "+EarEngine)