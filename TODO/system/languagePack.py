# language pack

languagePack=Language.lower()
languagePackLoaded=1

# we load default english language pack

for root, subdirs, files in os.walk(RuningFolder+'system/languagePack/en'):
  for name in files:
    if name.split(".")[-1] == "lang":
      execfile(os.path.join(root, name).encode('utf8'))
      if DEBUG==1:print "debug languagePack : ",os.path.join(root, name)

      
# we try to load user system language pack
  
if (os.path.isdir(RuningFolder+'system/languagePack/'+languagePack)):
  try:
    for root, subdirs, files in os.walk(RuningFolder+'system/languagePack/'+languagePack):
      for name in files:
        if name.split(".")[-1] == "lang":
          execfile(os.path.join(root, name).encode('utf8'))
          if DEBUG==1:print "debug user languagePack : ",os.path.join(root, name)
    
  except:
    languagePackLoaded=0
    pass
else:languagePackLoaded=0
i01.lang_shutDown=lang_shutDown