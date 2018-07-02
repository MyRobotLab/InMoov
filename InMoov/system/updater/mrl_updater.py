#mrl version check
#check if we are not using eclipse build
now = datetime.now()
if str(now.year)!=str(runtime.getVersion()[:4]) and str(runtime.getVersion()[:5])!="1.0.l":

  try:
    actualVersion=str(runtime.getVersion()[-4:])
  except:
    actualVersion=0
    pass
 
  currentMrlVersion=0
  iniFile=RuningFolder+'system/updater/currentMrlVersion.ini'

  currentMrlVersionCheck = ConfigParser.ConfigParser(allow_no_value = True)

  #default write current mrl version inside cfg file
  if not os.path.isfile(iniFile):
    currentMrlVersionCheck.add_section('CLIENT')
    currentMrlVersionCheck.set('CLIENT', 'currentMrlVersion',str(runtime.getVersion()[-4:]))
    with open(iniFile, 'w') as configfile:
      currentMrlVersionCheck.write(configfile)

  currentMrlVersionCheck.read(iniFile)
  currentMrlVersion=currentMrlVersionCheck.get('CLIENT', 'currentMrlVersion')

  #check if myrobotlab.jar version has changed
  #if yes we install mrl again

  if actualVersion!=currentMrlVersion and actualVersion!=0:
    try:
      SwingGui=Runtime.createAndStart("SwingGui", "SwingGui")
    except:
      pass

    #update version
    currentMrlVersionCheck.set('CLIENT', 'currentMrlVersion',str(runtime.getVersion()[-4:]))
    with open(iniFile, 'w') as configfile:
      currentMrlVersionCheck.write(configfile)
      
    #clean up mrl installation ( tell the .batch launcher to reinstall )
    open("mrlNeedReinstall", 'a').close()
    errorSpokenFunc('lang_newMRL')
    sleep(4)
    runtime.restart()
    #killRuntime()