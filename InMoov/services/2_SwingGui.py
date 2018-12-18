# ##############################################################################
#                 SWINGGUI SERVICE
# ##############################################################################
# 

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

if LaunchSwingGui:
  gui=Runtime.create("gui", "SwingGui")
  try:
    gui.setColor("Servo","0xB8A2A2")
    gui.setColor("Arduino","0x89A388")
    gui.setColor("VirtualArduino","0xAFBDAE")
    gui.setColor("Serial","0xD2E3D1")
    gui.setColor("OpenCV","0x9DAEC9")
    gui.setColor("WebkitSpeechRecognition","0xE7F2A2")
    gui.setColor("AudioFile","0xF4F5F0")
    gui.setColor("InMoov","0xF4F5F0")
    gui.setColor("InMoovHand","0xF4F5F0")
    gui.setColor("InMoovArm","0xF4F5F0")
    gui.setColor("InMoovHead","0xF4F5F0")
    gui.setColor("InMoovTorso","0xF4F5F0")
    gui.setColor("VoiceRss","0xF4F5F0")
    gui.setColor("Polly","0xF4F5F0")
    gui.setColor("MarySpeech","0xF4F5F0")
    gui.setColor("HtmlFilter","0xF4F5F0")
    gui.setColor("ImageDisplay","0xF4F5F0")
    gui.setColor("WikiDataFetcher","0xF4F5F0")
    gui.setColor("AzureTranslator","0xF4F5F0")
    gui.setColor("OpenWeatherMap","0xF4F5F0")
  except: 
      pass
  gui=Runtime.start("gui", "SwingGui")  
  #SwingGui.dockTab("python")
  print "MRL version : ",runtime.getVersion()[-4:]
  print "Inmoov version : ",version
  print "Starting..."