# -- coding: utf-8 --
# ##############################################################################
#                 MOUTH SERVICE FILE
# ##############################################################################

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
vocalError=False
try:
  i01.mouth=Runtime.start("i01.mouth", Speechengine)
except:pass

if not i01.mouth:
  vocalError=True
  i01.mouth=subconsciousMouth
  errorSpokenFunc('MyvoiceType')

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

    if 'oui ' in text or 'yes ' in text or ' oui' in text or 'ja ' in text or 'sim ' in text or text=="yes" or text=="kyllä":Yes()
    if 'non ' in text or 'no ' in text or 'nicht ' in text or 'neen ' in text or 'não ' in text or text=="no" or text=="ei":No()

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
  try:
    if Speechengine=="VoiceRss":i01.mouth.setKey(i01.mouth.VOICERSS_API_KEY,apiKey1)
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
    i01.mouth.setLanguage(Language)
  except:pass
  
setRobotLanguage()

#set CustomVoice
if not i01.mouth.setVoice(VoiceName):errorSpokenFunc('MyvoiceType')
#set english subconsious mouth to user globalised mouth now ( only if we found a language pack )
mouth=i01.startMouth()
python.subscribe(i01.mouth.getName(),"publishStartSpeaking")
python.subscribe(i01.mouth.getName(),"publishEndSpeaking")

try:
  i01.mouth.speak(",")
except:
  i01.mouth=subconsciousMouth
  vocalError=True
  errorSpokenFunc('VoiceRssNoWorky')
  pass
  
isReady=True
if Speechengine=="Polly" or Speechengine=="VoiceRss" or Speechengine=="IndianTts":isReady=mouth.isReady()
if not isReady:
  i01.mouth=subconsciousMouth
  vocalError=True
  errorSpokenFunc('VoiceRssNoWorky')

ear=i01.startEar()
if EarEngine=="WebkitSpeechRecognition":
  i01.ear.setContinuous(setContinuous)
  #start the browsers and show the WebkitSpeechRecognition service named i01.ear
  webgui = Runtime.create("webgui","WebGui")
  webgui.autoStartBrowser(False)
  webgui.startService()
  webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
  
python.subscribe(i01.ear.getName(),"recognized")
if not vocalError:subconsciousMouth.releaseService()
if languageError:errorSpokenFunc('MYLANGUAGE')
