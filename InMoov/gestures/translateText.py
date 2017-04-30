def translateText(text,language):
  
  
  RealLang="0"
  
  try:
    RealLang=en_languages[language]
  except: 
    inmoovSuper.getResponse("AZURE_ERROR_2 "+language)
  print RealLang
  
  try:
    AzureTranslator.detectLanguage(text)
  except:
    inmoovSuper.getResponse("AZURE_ERROR_1")
    RealLang="0"
  
  if RealLang!="0":
    AzureTranslator.toLanguage(RealLang)
    sleep(0.1)
    t_text=AzureTranslator.translate(text)
    
    #small trick to prevent connection timeout :)
    i=0
    while 'Cannot find an active Azure Market Place' in t_text and i<50: 
      print(i,t_text)
      i += 1 
      sleep(0.2)
      AzureTranslator.detectLanguage(text)
      t_text=AzureTranslator.translate(text+" ")
    
    
    if 'Cannot find an active Azure Market Place' in t_text:
      inmoovSuper.getResponse("AZURE_ERROR_3")
    else:
      mouth.setVoice(male_languages[RealLang])  
      print t_text
      talk(t_text)
      mouth.setVoice(Voice)
