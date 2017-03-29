#the function to download config file : getInmoovFrParameter('config',RuningFolder+"Inmoov.config")

def logIt(file,txt,method):
  with open(file,method) as filelog:
    filelog.write(txt+" \n")
    
logIt(RuningFolder+"system/inmoov.fr.log","Good evening Dave, ","w")

def getInmoovFrParameter(parameter,output):
  
  logIt(RuningFolder+"system/inmoov.fr.log","last action : "+str(datetime.now())+" : ","a")
  #user key?
  if glob.glob(RuningFolder+'*.key'):
    #cool !
    key=os.path.basename(glob.glob(RuningFolder+'*.key')[0]).split('.key', 1 )[0]
    tmpfile=output+".tmp"
    first_line=[""]
    third_line=[""]
    
    #ok try to fetch the file
    try:
      url="http://inmoov.fr/wp-content/themes/klein/buildconfigfile.php?nlcar=file&userid="+key+"&bodygroup="+parameter
      urlretrieve(url, tmpfile)
      logIt(RuningFolder+"system/inmoov.fr.log","fetch : "+url,"a")
    except:
      pass
    
    #ok check if there is a file downloaded
    if glob.glob(tmpfile):
      with open(tmpfile, 'r') as f:
        try:
          lines=f.readlines()
          first_line = lines[0]
          third_line = lines[2]
        except:
          pass
    
    #ok check if this is a real config file ( not a 404 or friend error ... )
    if first_line[0]==";" and third_line[0]!=";":
      shutil.move(tmpfile,output)
      url="http://inmoov.fr/wp-content/themes/klein/queuemsg.php?userid="+key+"&push=CONFUPDATE:"+parameter
      try:
        r=Parse(url)
        logIt(RuningFolder+"system/inmoov.fr.log",parameter+" >> "+ r,"a")
      except:
          logIt(RuningFolder+"system/inmoov.fr.log",parameter+" >> NO CONFIRMATION"+ r,"a")
          pass
      return True
    else:
      
      #ok there is problem, time to contact someone
      subconsciousMouth.speakBlocking('Alert ! Alert ! the config file ' + parameter + ' from inmoov web server cannot be parsed, please post your problem')
      logIt(RuningFolder+"system/inmoov.fr.log",parameter+" >> NOK","a")
      return False

  else:
    logIt(RuningFolder+"system/inmoov.fr.log","no key to parse : "+parameter,"a")
    return False
    
def talkToInmoovFrQueue(parameter):
    if glob.glob(RuningFolder+'*.key'):
    #cool !
      key=os.path.basename(glob.glob(RuningFolder+'*.key')[0]).split('.key', 1 )[0]
      url="http://inmoov.fr/wp-content/themes/klein/queuemsg.php?userid="+key+"&push="+parameter
      try:
        r=Parse(url)
        logIt(RuningFolder+"system/inmoov.fr.log","queue parameter : " + parameter + " >> "+ r,"a")
        return r
      except:
          logIt(RuningFolder+"system/inmoov.fr.log",url,"a")
          logIt(RuningFolder+"system/inmoov.fr.log",parameter+" >> NO CONFIRMATION"+ r,"a")
          pass
    
    
    
  


