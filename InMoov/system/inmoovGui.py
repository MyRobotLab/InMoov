

###############################################################################
#                 inmoov.fr connector
###############################################################################

#service configuration
####################
inmoovfrUrl="http://inmoov.fr/wp-content/themes/klein/"
if glob.glob(RuningFolder+'*.key'):
  key=os.path.basename(glob.glob(RuningFolder+'*.key')[0]).split('.key', 1 )[0]
  iHaveInmoovFrKey=1

#log function
#################### 
def logIt(file,txt,method):
  with open(file,method) as filelog:
    filelog.write(txt+" \n")
logIt(RuningFolder+"system/inmoov.fr.log","Good evening Dave, ","w")    

#config files update
####################
def getInmoovFrParameter(parameter,output):
#the function to download config file : getInmoovFrParameter('config',RuningFolder+"Inmoov.config")
  
  logIt(RuningFolder+"system/inmoov.fr.log","last action : "+str(datetime.now())+" : ","a")
  #user key?
  if iHaveInmoovFrKey:
    tmpfile=output+".tmp"
    first_line=[""]
    third_line=[""]
    
    #ok try to fetch the file
    try:
      url=inmoovfrUrl+"buildconfigfile.php?nlcar=file&userid="+key+"&bodygroup="+parameter
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
      url=inmoovfrUrl+"queuemsg.php?userid="+key+"&push=CONFUPDATED:"+parameter
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
 
#talk to seb
#################### 
def talkToInmoovFrQueue(parameter):
    if iHaveInmoovFrKey:
      url=inmoovfrUrl+"queuemsg.php?userid="+key+"&push="+parameter
      try:
        r=Parse(url)
        logIt(RuningFolder+"system/inmoov.fr.log","queue parameter : " + parameter + " >> "+ r,"a")
        return r
      except:
          logIt(RuningFolder+"system/inmoov.fr.log",url,"a")
          logIt(RuningFolder+"system/inmoov.fr.log",parameter+" >> NO CONFIRMATION"+ r,"a")
          pass
          
#get a job for the robot
#################### 
def getTheQueue():
   
  try:
    url = inmoovfrUrl+"queuemsg.php?userid="+key+"&mrlpullmsg=JSON&nbmsg=100"
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
  except:
    logIt(RuningFolder+"system/inmoov.fr.log","QUEUE ERROR >> "+ str(response),"a")
    return False
  
  return data
  
#function transformation
#################### 
def ROBOTSAY(what): 
  talkBlocking(what)
  
def UPDATECONF(what):
  print "TODO : UPDATECONF called"
  
def GESTURE(what):
  try:
    exec(what.split('.', 1 )[0]+'()')
  except:
    logIt(RuningFolder+"system/inmoov.fr.log","GESTURE ERROR >> "+ str(what),"a")
    return False
  
#time to loop
# ##############################################################################

if iHaveInmoovFrKey:
  inmoovfr = Runtime.start("inmoovfr","Clock")
  inmoovfr.setInterval(5000)

  def inmoovfr_def(timedata):
    if i01.RobotIsStarted and iHaveInmoovFrKey:
      talkToInmoovFrQueue("MRLALIVE:"+str(runtime.getVersion()[-4:]))
      talkToInmoovFrQueue("BATTERYLEVEL:"+str(batterieLevel))
      data=getTheQueue()
      if data:
        i=0
        for k in data:
          r=data[i]["message"].split(':', 1 )
          if len(r)>=2:
            functionToCall=r[0]
            parameterToCall=r[1]
            if functionToCall=="ROBOTSAY":ROBOTSAY(parameterToCall)
            if functionToCall=="GESTURE":GESTURE(parameterToCall)
            resp=talkToInmoovFrQueue("0&mrldelmsg="+data[i]["id"])
            logIt(RuningFolder+"system/inmoov.fr.log","queue : " + functionToCall + " >> "+ resp,"a")
          i+=1
      
  inmoovfr.addListener("pulse", python.name, "inmoovfr_def")    
  inmoovfr.startClock()
  
  
          
          
    
    
    
  


