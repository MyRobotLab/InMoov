# ##############################################################################
#            *** HEAD ***
# ##############################################################################



  
# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
isHeadActivated=0

#read current skeleton part config
ThisSkeletonPart=RuningFolder+'config/skeleton_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

###############################################################################
#                 webgui sync
getInmoovFrParameter('head',ThisSkeletonPart+'.config')
###############################################################################

try:
  CheckFileExist(ThisSkeletonPart)
  ThisSkeletonPartConfig = ConfigParser.ConfigParser()
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')

  isHeadActivated=ThisSkeletonPartConfig.getboolean('MAIN', 'isHeadActivated') 
  MouthControlActivated=ThisSkeletonPartConfig.getboolean('MOUTHCONTROL', 'MouthControlActivated')
  AudioSignalProcessing=ThisSkeletonPartConfig.getboolean('AUDIOSIGNALPROCESSING', 'AudioSignalProcessing')
  AnalogPinFromSoundCard=ThisSkeletonPartConfig.getint('AUDIOSIGNALPROCESSING', 'AnalogPin')
  if ScriptType=="Virtual":AnalogPinFromSoundCard=3
  HowManyPollsBySecond=ThisSkeletonPartConfig.getint('AUDIOSIGNALPROCESSING', 'HowManyPollsBySecond')
  MouthControlJawMin=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawMin')
  MouthControlJawMax=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawMax')
  
  try:
    MouthControlJawTweak=ThisSkeletonPartConfig.getboolean('MOUTHCONTROL', 'MouthControlJawTweak')
  except:
    ThisSkeletonPartConfig.set('MOUTHCONTROL', 'MouthControlJawTweak', False)
    ThisSkeletonPartConfig.set('MOUTHCONTROL', 'MouthControlJawdelaytime', 1) 
    ThisSkeletonPartConfig.set('MOUTHCONTROL', 'MouthControlJawdelaytimestop', 1) 
    ThisSkeletonPartConfig.set('MOUTHCONTROL', 'MouthControlJawdelaytimeletter', 1) 
    
    with open(ThisSkeletonPart+'.config', 'wb') as f:
      ThisSkeletonPartConfig.write(f)
    ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
    pass   
    
  MouthControlJawTweak=ThisSkeletonPartConfig.getboolean('MOUTHCONTROL', 'MouthControlJawTweak')
  MouthControlJawdelaytime=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytime')
  MouthControlJawdelaytimestop=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytimestop')
  MouthControlJawdelaytimeletter=ThisSkeletonPartConfig.getint('MOUTHCONTROL', 'MouthControlJawdelaytimeletter')
  jawMIN=ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw')
  jawMAX=ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw')
  neckRest=ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'neck')
  rotheadRest=ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rothead')
  neckPin=ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck')
except:
  isHeadActivated=0
  errorSpokenFunc('ConfigParserProblem','head.config')
  pass
 
#rollneck migration
try:
  tmprollneck = ThisSkeletonPartConfig.get('ROLLNECKSERVO', 'isRollNeckActivated')
except:
  ThisSkeletonPartConfig.set('SERVO_MINIMUM_MAP_OUTPUT', 'rollneck', 0)
  ThisSkeletonPartConfig.add_section('ROLLNECKSERVO')
  ThisSkeletonPartConfig.set('SERVO_MAXIMUM_MAP_OUTPUT', 'rollneck', 180)
  ThisSkeletonPartConfig.set('SERVO_REST_POSITION', 'rollneck', 90)
  ThisSkeletonPartConfig.set('SERVO_INVERTED', 'rollneck', 0)
  ThisSkeletonPartConfig.set('MINIMUM_MAP_INPUT', 'rollneck', 0)
  ThisSkeletonPartConfig.set('MAXIMUM_MAP_INPUT', 'rollneck', 180)
  ThisSkeletonPartConfig.set('MAX_VELOCITY', 'rollneck', -1)
  ThisSkeletonPartConfig.set('SERVO_PIN', 'rollneck', 30)
  ThisSkeletonPartConfig.set('ROLLNECKSERVO', 'isRollNeckActivated', True)
  ThisSkeletonPartConfig.set('ROLLNECKSERVO', 'RollNeckArduino', "left")
  
  with open(ThisSkeletonPart+'.config', 'wb') as f:
    ThisSkeletonPartConfig.write(f)
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
  pass 
  
try:
  rotheadEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rothead')
except:
  ThisSkeletonPartConfig.add_section('SERVO_AUTO_DISABLE')
  ThisSkeletonPartConfig.set('SERVO_AUTO_DISABLE', 'rothead', 1)
  ThisSkeletonPartConfig.set('SERVO_AUTO_DISABLE', 'rollneck', 1)
  ThisSkeletonPartConfig.set('SERVO_AUTO_DISABLE', 'jaw', 1)
  ThisSkeletonPartConfig.set('SERVO_AUTO_DISABLE', 'neck', 1)
  ThisSkeletonPartConfig.set('SERVO_AUTO_DISABLE', 'eyeX', 1)
  ThisSkeletonPartConfig.set('SERVO_AUTO_DISABLE', 'eyeY', 1)
  
  
  with open(ThisSkeletonPart+'.config', 'wb') as f:
    ThisSkeletonPartConfig.write(f)
  ThisSkeletonPartConfig.read(ThisSkeletonPart+'.config')
  pass 
isRollNeckActivated=ThisSkeletonPartConfig.getboolean('ROLLNECKSERVO', 'isRollNeckActivated') 
RollNeckArduino=ThisSkeletonPartConfig.get('ROLLNECKSERVO', 'RollNeckArduino')

# ##############################################################################
#                 SERVO FUNCTIONS
# ##############################################################################

if isHeadActivated==1 and (ScriptType=="LeftSide" or ScriptType=="Full") or ScriptType=="Virtual":
  if LeftPortIsConnected:
    talkEvent(lang_startingHead)
    head = Runtime.create("i01.head","InMoovHead")
    #map    
    head.jaw.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'jaw'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'jaw')) 
    head.eyeX.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyeX'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyeX')) 
    head.eyeY.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'eyeY'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'eyeY')) 
    head.neck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'neck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'neck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'neck')) 
    head.rothead.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rothead'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rothead'))
    head.rollNeck.map(ThisSkeletonPartConfig.getint('MINIMUM_MAP_INPUT', 'rollneck'),ThisSkeletonPartConfig.getint('MAXIMUM_MAP_INPUT', 'rollneck'),ThisSkeletonPartConfig.getint('SERVO_MINIMUM_MAP_OUTPUT', 'rollneck'),ThisSkeletonPartConfig.getint('SERVO_MAXIMUM_MAP_OUTPUT', 'rollneck'))
    
    #velocity
    #head.jaw.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'jaw'))
    #head.eyeX.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'eyeX'))
    #head.eyeY.setVelocity(ThisSkeletonPartConfig.getint('VELOCITY', 'eyeY'))
  
    #maxvelocity
    head.neck.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'neck'))
    head.rothead.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rothead'))
    head.rollNeck.setMaxVelocity(ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rollneck'))
     
    head.jaw.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'jaw'))
    head.eyeX.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyeX'))
    head.eyeY.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'eyeY'))
    head.neck.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'neck'))
    head.rothead.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rothead'))
    head.rollNeck.setRest(ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rollneck'))
  
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'jaw'):head.jaw.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyeX'):head.eyeX.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'eyeY'):head.eyeY.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'neck'):head.neck.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rothead'):head.rothead.setInverted(True)
    if ThisSkeletonPartConfig.getboolean('SERVO_INVERTED', 'rollneck'):head.rollNeck.setInverted(True)

    i01.startHead(MyLeftPort,BoardTypeMyLeftPort,ThisSkeletonPartConfig.getint('SERVO_PIN', 'neck'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'rothead'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeX'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'eyeY'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'jaw'),ThisSkeletonPartConfig.getint('SERVO_PIN', 'rollneck'))
    rollneck=head.rollNeck
    
    #overide rollneck arduino
    try:
      RollNeckArduino=eval(RollNeckArduino)
    except:
      errorSpokenFunc('BAdrduinoChoosen',', Roll Neck')
      isRollNeckActivated=0
      pass  
    
    if isRollNeckActivated:
      head.rollNeck.detach(left)
      head.rollNeck.attach(RollNeckArduino,ThisSkeletonPartConfig.getint('SERVO_PIN', 'rollNeck'),ThisSkeletonPartConfig.getint('SERVO_REST_POSITION', 'rollNeck'),ThisSkeletonPartConfig.getint('MAX_VELOCITY', 'rollNeck'))
     
    
    
    head.enableAutoEnable(1)
  
    rotheadEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rothead')
    neckEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'neck')
    rollneckEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'rollneck')
    eyeXEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyeX')
    eyeYEnableAutoDisable=ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'eyeY')
    head.rothead.enableAutoDisable(rotheadEnableAutoDisable)
    head.neck.enableAutoDisable(neckEnableAutoDisable)
    head.rollNeck.enableAutoDisable(rollneckEnableAutoDisable)
    head.jaw.enableAutoDisable(ThisSkeletonPartConfig.getboolean('SERVO_AUTO_DISABLE', 'jaw'))
    head.eyeX.enableAutoDisable(eyeXEnableAutoDisable)
    head.eyeY.enableAutoDisable(eyeYEnableAutoDisable)
    
    
    head.jaw.setVelocity(-1)
    head.rest()
    
# ##############################################################################
#                 Software mouth control
# ##############################################################################    
    
    if MouthControlActivated and AudioSignalProcessing==False:
      #MouthControl = Runtime.createAndStart("i01.mouthControl","MouthControl")
      i01.startMouthControl(MyLeftPort)
      i01.mouthControl.setmouth(MouthControlJawMin,MouthControlJawMax)
      print "software mouthcontrol activation"
      if MouthControlJawTweak:i01.mouthControl.setDelays(MouthControlJawdelaytime, MouthControlJawdelaytimestop, MouthControlJawdelaytimeletter)
      talkEvent(lang_startingMouth)
# ##############################################################################
#                 mouth control based on audio signal processing
# ##############################################################################  
    
    #please set aref
    if AudioSignalProcessing:
      left.addListener("publishPinArray","python","publishMouthcontrolPinLeft")
      AudioSignalProcessing=False
      MouthControlActivated=False
      AudioSignalProcessingCalibration=1
      left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
      talkBlocking(lang_MouthSyncronisation)
      
      
      AudioSignalProcessingCalibration=0
      maxAudioValue=maxAverage(AudioInputValues,10)
      AudioInputValues=[]
      AudioSignalProcessingCalibration=1
      sleep(3)
      AudioSignalProcessingCalibration=0
      minAudioValue = (sum(AudioInputValues) / len(AudioInputValues)) + 20
      left.disablePin(AnalogPinFromSoundCard)
      result=0
      #arduino dit not detect analog value
      if minAudioValue>50:
        talkBlocking(lang_MouthSyncronisationBad+str(AnalogPinFromSoundCard))
        result=1
      #arduino detect a poor value
      if result==0 and (maxAudioValue-minAudioValue<=255):
        head.jaw.map(minAudioValue,maxAudioValue,jawMIN,jawMAX)
        AudioSignalProcessing=True
        talkBlocking(lang_MouthSyncronisationNotPerfect)
      #arduino detect a good value  
      if result==0 and (maxAudioValue-minAudioValue>255):
        head.jaw.map(minAudioValue,maxAudioValue,jawMIN,jawMAX)
        AudioSignalProcessing=True
        talkBlocking(lang_MouthSyncronisationOk)
        
      print maxAudioValue,minAudioValue
      
    
    #tracking
    if opencvStarted:
      i01.startEyesTracking(MyLeftPort,22,24)
      i01.startHeadTracking(MyLeftPort,12,13)
      talkBlocking(lang_TrackingStarted)  
    
    
  else:
    #we force parameter if arduino is off
    isHeadActivated=0
    MouthControlActivated=0
    
else:
  MouthControlActivated=0
    
#todo set inverted
