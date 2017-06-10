#mrl version check
#check if we are not using eclipse build
now = datetime.now()
if str(now.year)!=str(runtime.getVersion()[:4]):
  print

  actualVersion=int(runtime.getVersion()[-4:])

  currentMrlVersion=0
  iniFile=RuningFolder+'system/updater/currentMrlVersion.ini'

  currentMrlVersionCheck = ConfigParser.ConfigParser(allow_no_value = True)

  #default write current mrl version inside cfg file
  if not os.path.isfile(iniFile):
    currentMrlVersionCheck.add_section('CLIENT')
    currentMrlVersionCheck.set('CLIENT', 'currentMrlVersion',int(runtime.getVersion()[-4:]))
    with open(iniFile, 'w') as configfile:
      currentMrlVersionCheck.write(configfile)

  currentMrlVersionCheck.read(iniFile)
  currentMrlVersion=currentMrlVersionCheck.getint('CLIENT', 'currentMrlVersion')

  #check if myrobotlab.jar version has changed
  #if yes we install mrl again

  if actualVersion!=currentMrlVersion:
    try:
      SwingGui=Runtime.createAndStart("SwingGui", "SwingGui")
    except:
      pass

    #update version
    currentMrlVersionCheck.set('CLIENT', 'currentMrlVersion',int(runtime.getVersion()[-4:]))
    with open(iniFile, 'w') as configfile:
      currentMrlVersionCheck.write(configfile)
      
    #clean up mrl installation ( tell the .batch launcher to reinstall )
    open("mrlNeedReinstall", 'a').close()
    errorSpokenFunc('lang_newMRL')
    sleep(4)
    killRuntime()