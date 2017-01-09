def translateText(text,language):
	
	AzureTranslator.detectLanguage(text)
	RealLang="0"
	try:
		RealLang=en_languages[language]
	except: 
		chatBot.getResponse("AZURE_ERROR_2 "+language)
	print RealLang
	if RealLang!="0":
		AzureTranslator.toLanguage(RealLang)
		t_text=AzureTranslator.translate(text)   
		if 'Cannot find an active Azure Market Place' in t_text:
			sleep(0.5)
			t_text=AzureTranslator.translate(text)
		if 'Cannot find an active Azure Market Place' in t_text:
			chatBot.getResponse("AZURE_ERROR_1")
		else:
			mouth.setVoice(male_languages[RealLang])  
			print t_text
			talk(t_text)
			mouth.setVoice(Voice)