#CREDITS : PAPAOUTAI
# your keys here ( put in config file ) : https://datamarket.azure.com/dataset/bing/microsofttranslator 

AzureTranslator=Runtime.createAndStart("AzureTranslator", "AzureTranslator")
sleep(0.1)
#initiate azure
#AzureTranslator.setCredentials(Azure_client_id,Azure_client_secret)
AzureTranslator.setCredentials("90a98ba0-a028-4b61-9e7a-10a22b186944","SZDqSTcKxwUMiPEievXKWleXAYMWuD1Tm1D2igskvus") # KEY and SECRET azure credentials


#Origin language 
supported_languages = { # as defined here: http://msdn.microsoft.com/en-us/library/hh456380.aspx
    'ar' : ' Arabic',
 #   'bs-Latn' : 'Bosnian (Latin)',
 #  'bg' : 'Bulgarian',
 #   'ca' : 'Catalan',
 #   'zh-CHS' : 'Chinese (Simplified)',
 #   'zh-CHT' : 'Chinese (Traditional)',
 #   'hr' : 'Croatian',
 #   'cs' : 'Czech',
    'da' : 'Danish',
    'nl' : 'Dutch',
    'en' : 'English',
 #  'et' : 'Estonian',
 #  'fi' : 'Finnish',
    'fr' : 'French',
    'de' : 'German',
    'el' : 'Greek',
 #  'ht' : 'Haitian Creole',
 #  'he' : 'Hebrew',
 #  'hi' : 'Hindi',
 #  'mww' : 'Hmong Daw',
 #  'hu' : 'Hungarian',
 #  'id' : 'Indonesian',
    'it' : 'Italian',
 #  'ja' : 'Japanese',
 #  'sw' : 'Kiswahili',
 #  'tlh' : 'Klingon',
 #  'ko' : 'Korean',
 #  'lv' : 'Latvian',
 #  'lt' : 'Lithuanian',
 #  'ms' : 'Malay',
 #  'mt' : 'Maltese',
    'no' : 'Norwegian',
 #  'fa' : 'Persian',
 #  'pl' : 'Polish',
    'pt' : 'Portuguese',
 #  'ro' : 'Romanian',
    'ru' : 'Russian',
 #  'sr-Cyrl' : 'Serbian (Cyrillic)',
 #  'sr-Latn' : 'Serbian (Latin)',
 #  'sk' : 'Slovak',
 #  'sl' : 'Slovenian',
    'es' : 'Spanish',
    'sv' : 'Swedish',
 #  'th' : 'Thai',
 #  'tr' : 'Turkish',
 #  'uk' : 'Ukrainian',
 #  'ur' : 'Urdu',
 #  'vi' : 'Vietnamese',
 #  'cy' : 'Welsh',
 #  'yua' : 'Yucatec Maya',
}

#acapela voice name map 
male_languages = { 
    'ar' : 'Nizar',
    'da' : 'Rasmus',
    'nl' : 'Jeroen',
    'en' :  Voice,
    'fr' : 'Bruno',
    'de' : 'Klaus',
    'el' : 'Dimitris',
    'it' : 'Vittorio',
    'no' : 'Olav',
    'es' : 'Antonio',
    'sv' : 'Emil',
	'ja' : 'Sakura',
	'pt' : 'Celia',
	'ru' : 'Alyona',
}

female_languages = { 
    'pt' : 'Celia',
	'ru' : 'Alyona',
}

#Translate to :
en_languages = {
    'arab' : 'ar',
	'arabe' : 'ar',
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
    'greek' : 'el',
    'italian' : 'it',
    'norwegian' : 'no',
    'norvegien' : 'no',
    'spanish' : 'es',
    'espagnol' : 'es',
    'swedish' : 'sv',
    'suedois' : 'sv',
	'japonese' : 'ja',
	'portuguese' : 'pt',
	'portuguais' : 'pt',
	'russian' : 'ru',
	'russe' : 'ru',
	
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
			mouth.setVoice(Voice)

			
			

