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
try:
  test=ThisServicePartConfig.get('MAIN', 'outputSpeechService')
except:
  ThisServicePartConfig.set('MAIN', 'outputSpeechService', 'default')
  with open(ThisServicePart+'.config', 'wb') as f:
    ThisServicePartConfig.write(f)
  ThisServicePartConfig.read(ThisServicePart+'.config')
  pass
outputSpeechService=ThisServicePartConfig.get('MAIN', 'outputSpeechService')

# ##############################################################################
#                 SERVICE START
# ##############################################################################

AzureTranslator=Runtime.createAndStart("AzureTranslator", "AzureTranslator")



# we map AzureTranslator output to an other speech service
if outputSpeechService!="default":
  AzureTranslatorMouth = Runtime.createAndStart("AzureTranslatorMouth", outputSpeechService)
  #maybe
  #AzureTranslatorMouth.setKey(awsaccesskeyid,awssecretkey)
  python.subscribe(AzureTranslatorMouth.getName(),"publishStartSpeaking")
  python.subscribe(AzureTranslatorMouth.getName(),"publishEndSpeaking")
else:
  # or we map AzureTranslator output to original mouth
  AzureTranslatorMouth=mouth
  outputSpeechService=Speechengine

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


#zombie natural voices 
male_languagesNatural = { 
  'da' : 'Danish_Mikkel',
  'nl' : 'German_Johann',
  'en' : 'US-English_Ronald',
  'fr' : 'French_Gabriel',
  'de' : 'Dutch_Daan',
  'it' : 'Italian_Francesco',
  'is' : 'Icelandic_Gunnar',
  'no' : 'Norwegian_Ingrid',
  'pt' : 'Portuguese_Joao ',
  'ru' : 'Russian_Sergei',
  'es' : 'Spanish_Enrique',
  'sv' : 'Swedish_Elsa',
  'tr' : 'Turkish_Esma',
  'ro' : 'Romanian_Elena',
  'ja' : 'Japanese_Takumi',
  'pl' : 'Polish_Kacper',
}

female_languagesNatural = { 
  'da' : 'Danish_Line',
  'nl' : 'German_Johann',
  'en' : 'US-English_Linda',
  'fr' : 'French_Renee',
  'de' : 'Dutch_Birgit',
  'it' : 'Italian_Giulia',
  'is' : 'Icelandic_Helga',
  'no' : 'Norwegian_Ingrid',
  'pt' : 'Portuguese_Mariana',
  'ru' : 'Russian_Olga',
  'es' : 'Spanish_Laura',
  'sv' : 'Swedish_Elsa',
  'tr' : 'Turkish_Esma',
  'ro' : 'Romanian_Elena',
  'ja' : 'Japanese_Midori',
  'pl' : 'Polish_Zofia',
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
if outputSpeechService=="MarySpeech":
  translatorDegraded=1
  male_languages=male_languagesMary
  female_languages=female_languagesMary
  
if outputSpeechService=="NaturalReaderSpeech":
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
  
  if outputSpeechService=="MarySpeech":  
    if not CheckMaryTTSVoice("dfki-pavoque-neutral-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      AzureTranslatorMouth.installComponentsAcceptLicense("dfki-pavoque-neutral-hsmm")
      needArestart=1
    if not CheckMaryTTSVoice("upmc-jessica-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)      
      AzureTranslatorMouth.installComponentsAcceptLicense("upmc-jessica-hsmm")  
      needArestart=1
    if not CheckMaryTTSVoice("upmc-pierre-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      AzureTranslatorMouth.installComponentsAcceptLicense("upmc-pierre-hsmm") 
      needArestart=1
    if not CheckMaryTTSVoice("istc-lucia-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      AzureTranslatorMouth.installComponentsAcceptLicense("istc-lucia-hsmm") 
      needArestart=1
    if not CheckMaryTTSVoice("dfki-ot-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      AzureTranslatorMouth.installComponentsAcceptLicense("dfki-ot-hsmm")
      needArestart=1
    if not CheckMaryTTSVoice("bits1-hsmm"):
      if needAdownloadTalk:
        needAdownloadTalk=0
        talkBlocking(lang_MaryDownloadAll)
      AzureTranslatorMouth.installComponentsAcceptLicense("bits1-hsmm")
      needArestart=1
    
    if needArestart:
      errorSpokenFunc('VoiceDownloaded')
      sleep(4)
      runtime.shutdown()
    
  if outputSpeechService=="Polly" or outputSpeechService=="MarySpeech" or outputSpeechService=="NaturalReaderSpeech":
    RealLang="0"
    
    try:
      RealLang=en_languages[language]
    except:
      chatBot.setPredicate(chatBot.currentUserName,"topic","default")
      chatBot.getResponse("AZURE_ERROR_2 "+language)
    print RealLang
    
    try:
      AzureTranslator.detectLanguage(text)
    except:
      chatBot.setPredicate(chatBot.currentUserName,"topic","default")
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
        chatBot.setPredicate(chatBot.currentUserName,"topic","default")
        chatBot.getResponse("AZURE_ERROR_3")
      else:
        AzureTranslatorMouth.setVoice(unicode(ttsVoiceGender[RealLang],'utf-8'))  
        print t_text
        AzureTranslatorMouth.speakBlocking(unicode(t_text,'utf-8'))
        #restore original VoiceName
        mouth.setVoice(VoiceName)        
  else:
    talk(lang_PollyNeeded)