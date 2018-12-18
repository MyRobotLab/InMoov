# we try to load user system language pack
  
if (os.path.isdir(RuningFolder+'system/languagePack/'+Language)):
  try:
    #push local yolo dictionary
    shutil.copy(RuningFolder+'system/languagePack/'+Language+'/coco.names',os.getcwd().replace("\\", "/")+"/yolo/coco.names")
    #other translations   
  except:
    pass
