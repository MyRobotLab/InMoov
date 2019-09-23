# ##############################################################################
#                 AUDIOFILE SERVICE
# ##############################################################################
# http://myrobotlab.org/service/audiofile

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

MyMusicPath=ThisServicePartConfig.get('AUDIO', 'MyMusicPath')

#for noworky
log.info("MyMusicPath : "+str(MyMusicPath))
musicpath = MyMusicPath


#startup sound
AudioPlayer = Runtime.createAndStart("AudioPlayer", "AudioFile")
mouthControlAudiofile=True

def onAudioStart(data):
  try:
    if ear.listening:
      ear.setAutoListen(False)
      ear.stopListening()
  except:
    pass
  
  if AudioSignalProcessing and isHeadActivated:
    print "onaudiostart"
    try:
      head.jaw.moveTo(180)
      left.enablePin(AnalogPinFromSoundCard,HowManyPollsBySecond)
    except:
      print "onAudioStart error"
      pass
      
  try:
    if MouthControlActivated and mouthControlAudiofile:i01.mouthControl.onStartSpeaking("This is a fake text, a long fake text, very long.")
  except:
    pass
    

def onAudioEnd(data):
  try:
    if not ear.listening:
      ear.setAutoListen(setAutoListen)
      ear.startListening()
  except:
    print "onAudioEnd error"
    pass
  if AudioSignalProcessing and isHeadActivated:
    try:
      left.disablePin(AnalogPinFromSoundCard)
      #head.jaw.detach()
    except:
      print "onAudioEnd error"
      pass
      
  try:
    if MouthControlActivated and mouthControlAudiofile:i01.mouthControl.onEndSpeaking("This is a fake text, a long fake text, very long.")
  except:
    pass
  
def AudioPlay(file):
  AudioPlayer.playFile(file,False)
      

if StartupSound:AudioPlayer.playFileBlocking(RuningFolder+'/system/sounds/startupsound.mp3')
python.subscribe(AudioPlayer.getName(),"publishAudioStart")
python.subscribe(AudioPlayer.getName(),"publishAudioEnd")

# play a song from your music directory
def play():
    global musiconoff
    musiconoff = 1
    #musicpath = (RuningFolder+"/system/sounds/")
    files = os.listdir(musicpath)
    song=random.choice(files)
    sleep(3)
    #i01.mouth.speakBlocking("playing song" + str(song))
    AudioPlayer.playFile(musicpath + str(song) , False)
    print("playing song:" + str(song))
    sleep(1)
    ear.startListening()
    ear.setAutoListen(True)

def nextMusic():
    if musiconoff == 1:
        AudioPlayer.stop()
        print "next music" 
        play()

# pause method 
def pause():
    if musiconoff == 1:
      AudioPlayer.pause()
      print "set music on pause"

# resume method 
def resume():
    if musiconoff == 1:
      AudioPlayer.resume()
      print "resuming music"
        
# stopped method is called when at the end of an audio file
def stop():
    if musiconoff == 1:
        AudioPlayer.stop()
        print "stop playing"
