#the function to download config file : getInmoovFrParameter(key,'config',RuningFolder+"Inmoov.config")

def getInmoovFrParameter(parameter,output):
  
 
  #user key?
  if glob.glob(RuningFolder+'*.key'):
    #cool !
    key=os.path.basename(glob.glob(RuningFolder+'*.key')[0]).split('.key', 1 )[0]
    tmpfile=output+".tmp"
    first_line=[""]
    third_line=[""]
    
    #ok try to fetch the file
    try:
      urlretrieve("http://inmoov.fr/wp-content/themes/klein/buildconfigfile.php?nlcar=file&userid="+key+"&bodygroup="+parameter, tmpfile)
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
      return True
    else:
      
      #ok there is problem, time to contact someone
      subconsciousMouth.speakBlocking('Alert ! Alert ! the config file ' + parameter + ' from inmoov web server cannot be parsed, please post your problem')
      print "f1",first_line
      print "f3",third_line
      return False

  else:
    print "no inmoov.fr key"
    return False


