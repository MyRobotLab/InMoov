def RemoveFile(file):
  try:
    os.remove(file)
  except:
    pass
  
RemoveFile(RuningFolder+"life/AutoListen.py")

  #clean up .default.config
for root, subdirs, files in os.walk(RuningFolder):
  for name in files:
    if name.split(".")[-1] == "default":
      os.remove(os.path.join(root, name))
      if DEBUG==1:print "removed .default : ",os.path.join(root, name)