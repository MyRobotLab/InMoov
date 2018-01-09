# ##############################################################################
#                 SWINGGUI SERVICE
# ##############################################################################
# 

# ##############################################################################
# MRL SERVICE CALL
# ##############################################################################

if LaunchSwingGui:
  SwingGui=Runtime.create("SwingGui", "SwingGui")
  try:
    SwingGui.setColor("Servo","0xB8A2A2")
    SwingGui.setColor("Arduino","0x89A388")
    SwingGui.setColor("VirtualArduino","0xAFBDAE")
    SwingGui.setColor("Serial","0xD2E3D1")
    SwingGui.setColor("OpenCV","0x9DAEC9")
    SwingGui.setColor("WebkitSpeechRecognition","0xE7F2A2")
    SwingGui.setColor("AudioFile","0xF4F5F0")
    SwingGui.setColor("InMoov","0xF4F5F0")
    SwingGui.setColor("InMoovHand","0xF4F5F0")
    SwingGui.setColor("InMoovArm","0xF4F5F0")
    SwingGui.setColor("InMoovHead","0xF4F5F0")
    SwingGui.setColor("InMoovTorso","0xF4F5F0")
    SwingGui.setColor("VoiceRss","0xF4F5F0")
    SwingGui.setColor("Polly","0xF4F5F0")
    SwingGui.setColor("MarySpeech","0xF4F5F0")
    SwingGui.setColor("HtmlFilter","0xF4F5F0")
    SwingGui.setColor("ImageDisplay","0xF4F5F0")
    SwingGui.setColor("WikiDataFetcher","0xF4F5F0")
    SwingGui.setColor("AzureTranslator","0xF4F5F0")
    SwingGui.setColor("OpenWeatherMap","0xF4F5F0")
  except: 
      pass
    
  SwingGui=Runtime.start("SwingGui", "SwingGui")
  #SwingGui.dockTab("python")
  print "MRL version : ",runtime.getVersion()[-4:]
  print "Inmoov version : ",version
  print "Starting..."