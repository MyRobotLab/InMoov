# -- coding: utf-8 --
# ##############################################################################
#                 AZURE TRANSLATOR FILE
# ##############################################################################


#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
UseMaleVoice=ThisServicePartConfig.getboolean('MAIN', 'UseMaleVoice')
apikey=ThisServicePartConfig.get('MAIN', 'apikey')

AzureTranslator=Runtime.createAndStart("AzureTranslator", "AzureTranslator")
#initiate azure

if apikey!="":AzureTranslator.setCredentials(apikey)


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

#Mary tts voice name map 
male_languagesMary = { 
  'da' : 'dfki-pavoque-neutral-hsmm',
  'nl' : 'dfki-pavoque-neutral-hsmm',
  'en' : 'cmu-bdl-hsmm',
  'fr' : 'upmc-pierre-hsmm',
  'de' : 'dfki-pavoque-neutral-hsmm',
  'it' : 'istc-lucia-hsmm',
  'is' : 'dfki-pavoque-neutral-hsmm',
  'no' : 'dfki-pavoque-neutral-hsmm',
  'pt' : 'istc-lucia-hsmm',
  'ru' : 'cmu-bdl-hsmm',
  'es' : 'istc-lucia-hsmm',
  'sv' : 'cmu-bdl-hsmm',
  'tr' : 'dfki-ot-hsmm',
  'ro' : 'cmu-bdl-hsmm',
  'ja' : 'cmu-bdl-hsmm',
  'pl' : 'cmu-bdl-hsmm',
}

female_languagesMary = { 
  'da' : 'cmu-bdl-hsmm',
  'nl' : 'dfki-pavoque-neutral-hsmm',
  'en' : 'cmu-slt-hsmm',
  'fr' : 'upmc-jessica-hsmm',
  'de' : 'bits1-hsmm',
  'it' : 'istc-lucia-hsmm',
  'is' : 'cmu-bdl-hsmm',
  'no' : 'cmu-bdl-hsmm',
  'pt' : 'istc-lucia-hsmm',
  'ru' : 'cmu-bdl-hsmm',
  'es' : 'istc-lucia-hsmm',
  'sv' : 'cmu-bdl-hsmm',
  'tr' : 'dfki-ot-hsmm',
  'ro' : 'cmu-bdl-hsmm',
  'ja' : 'cmu-bdl-hsmm',
  'pl' : 'cmu-bdl-hsmm',
}


#experimental natural voices 
male_languagesNatural = { 
  'da' : 'Erik',
  'nl' : 'Klaus',
  'en' : 'Ryan',
  'fr' : 'Bruno',
  'de' : 'Klaus',
  'it' : 'Vittorio',
  'is' : 'Erik',
  'no' : 'Erik',
  'pt' : 'Celia ',
  'ru' : 'Ryan',
  'es' : 'Alberto',
  'sv' : 'Erik',
  'tr' : 'Ryan',
  'ro' : 'Ryan',
  'ja' : 'Sakura',
  'pl' : 'Ryan',
}

female_languagesNatural = { 
  'da' : 'Emma',
  'nl' : 'Klaus',
  'en' : 'Crystal',
  'fr' : 'Louise',
  'de' : 'Klaus',
  'it' : 'Chiara',
  'is' : 'Emma',
  'no' : 'Emma',
  'pt' : 'Celia',
  'ru' : 'Ryan',
  'es' : 'Rosa',
  'sv' : 'Emma',
  'tr' : 'Ryan',
  'ro' : 'Ryan',
  'ja' : 'Sakura',
  'pl' : 'Ryan',
}

#Translate to :
#TODO ADD TRANSLATED KEYWORDS
en_languages = {
  'danish' : 'da',
  'danois' : 'da',
  'dutch' : 'nl',
  'hollandais' : 'nl',
  'english' : 'en',
  'anglais' : 'en',
  'french' : 'fr',
  'français' : 'fr',
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
  'japonais' : 'ja',
  'portuguese' : 'pt',
  'portuguais' : 'pt',
  'turkish' : 'tr',
  'turk' : 'tr',
  'russian' : 'ru',
  'russe' : 'ru',
  'romanian' : 'ro',
  'roumain' : 'ro',
  
}

global translatorDegraded
translatorDegraded=0
if MyvoiceTTS=="MarySpeech":
  translatorDegraded=1
  male_languages=male_languagesMary
  female_languages=female_languagesMary
  
if MyvoiceTTS=="NaturalReaderSpeech":
  translatorDegraded=0
  male_languages=male_languagesNatural
  female_languages=female_languagesNatural
  
if UseMaleVoice:
  ttsVoiceGender=male_languages
else:
  ttsVoiceGender=female_languages

def translateText(text,language):
  global translatorDegraded
  needArestart=0
  needAdownloadTalk=1
  if translatorDegraded:
    translatorDegraded=0
    talkBlocking(lang_MaryTranslator)
  
  if MyvoiceTTS=="MarySpeech":  
    if not CheckMaryTTSVoice("dfki-pavoque-neutral-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      mouth.installComponentsAcceptLicense("dfki-pavoque-neutral-hsmm")
      needArestart=1
    if not CheckMaryTTSVoice("upmc-jessica-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)      
      mouth.installComponentsAcceptLicense("upmc-jessica-hsmm")  
      needArestart=1
    if not CheckMaryTTSVoice("upmc-pierre-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      mouth.installComponentsAcceptLicense("upmc-pierre-hsmm") 
      needArestart=1
    if not CheckMaryTTSVoice("istc-lucia-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      mouth.installComponentsAcceptLicense("istc-lucia-hsmm") 
      needArestart=1
    if not CheckMaryTTSVoice("dfki-ot-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      mouth.installComponentsAcceptLicense("dfki-ot-hsmm")
      needArestart=1
    if not CheckMaryTTSVoice("bits1-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      mouth.installComponentsAcceptLicense("bits1-hsmm")
      needArestart=1
    
    if needArestart:
      errorSpokenFunc('VoiceDownloaded')
      sleep(4)
      runtime.exit()
    
  if MyvoiceTTS=="Polly" or MyvoiceTTS=="MarySpeech" or MyvoiceTTS=="NaturalReaderSpeech":
    RealLang="0"
    
    try:
      RealLang=en_languages[language]
    except: 
      chatBot.getResponse("AZURE_ERROR_2 "+language)
    print RealLang
    
    try:
      AzureTranslator.detectLanguage(text)
    except:
      chatBot.getResponse("AZURE_ERROR_1")
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
        chatBot.getResponse("AZURE_ERROR_3")
      else:
        mouth.setVoice(unicode(ttsVoiceGender[RealLang],'utf-8'))  
        print t_text
        talkBlocking(t_text)
        mouth.setVoice(unicode(MyvoiceType,'utf-8'))
        
  else:
    talk(lang_PollyNeeded)