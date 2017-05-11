# -- coding: utf-8 --
# ##############################################################################
#                 AZURE TRANSLATOR FILE
# ##############################################################################


#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
UseMaleVoice=ThisServicePartConfig.get('MAIN', 'UseMaleVoice')
apikey=ThisServicePartConfig.get('MAIN', 'apikey')

AzureTranslator=Runtime.createAndStart("AzureTranslator", "AzureTranslator")
#initiate azure
AzureTranslator.setCredentials(apikey)


#Origin language 
supported_languages = { # as defined here: http://msdn.microsoft.com/en-us/library/hh456380.aspx
  'da' : 'Danish',
  'nl' : 'Dutch',
  'en' : 'English',
  'fr' : 'French',
  'de' : 'German',
  'it' : 'Italian',
  'is' : 'Iceland',
  'no' : 'Norwegian',
  'pt' : 'Portuguese',
  'ru' : 'Russian',
  'es' : 'Spanish',
  'sv' : 'Swedish',
  'tr' : 'Turkish',
  'ro' : 'Romanian',
  'ja' : 'Japanese',
  'pl' : 'Polish',
}

#polly voice name map 
male_languages = { 
  'da' : 'Mads',
  'nl' : 'Ruben',
  'en' : 'Joey',
  'fr' : 'Mathieu',
  'de' : 'Hans',
  'it' : 'Giorgio',
  'is' : 'Karl',
  'no' : 'Liv',
  'pt' : 'Cristiano',
  'ru' : 'Maxim',
  'es' : 'Enrique',
  'sv' : 'Astrid',
  'tr' : 'Filiz',
  'ro' : 'Carmen',
  'ja' : 'Mizuki',
  'pl' : 'Jacek',
}

female_languages = { 
  'da' : 'Naja',
  'nl' : 'Lotte',
  'en' : 'Joanna',
  'fr' : 'Céline',
  'de' : 'Marlene',
  'it' : 'Carla',
  'is' : 'Dóra',
  'no' : 'Liv',
  'pt' : 'Inês',
  'ru' : 'Tatyana',
  'es' : 'Conchita',
  'sv' : 'Astrid',
  'tr' : 'Filiz',
  'ro' : 'Carmen',
  'ja' : 'Mizuki',
  'pl' : 'Ewa',
}

#Translate to :
en_languages = {
  'danish' : 'da',
  'danois' : 'da',
  'dutch' : 'nl',
  'hollandais' : 'nl',
  'english' : 'en',
  'anglais' : 'en',
  'french' : 'fr',
  'francais' : 'fr',
  'german' : 'de',
  'allemand' : 'de',
  'italian' : 'it',
  'italien' : 'it',
  'norwegian' : 'no',
  'norvegien' : 'no',
  'Icelandic' : 'is',
  'islandais' : 'is',
  'spanish' : 'es',
  'espagnol' : 'es',
  'swedish' : 'sv',
  'suédois' : 'sv',
  'japonese' : 'ja',
  'Japonais' : 'ja',
  'portuguese' : 'pt',
  'portuguais' : 'pt',
  'turkish' : 'tr',
  'turk' : 'tr',
  'russian' : 'ru',
  'russe' : 'ru',
  'romanian' : 'ro',
  'roumain' : 'ro',
  
}

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
      mouth.setVoice(MyvoiceType)

      
      
