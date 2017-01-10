# -- coding: utf-8 --
# ##############################################################################
# ERRORS FILE
# ##############################################################################



def errorSpokenFunc(errorType,param="0"):
	global RobotIsErrorMode
	if errorType!="BadLanguagePack":
		RobotIsErrorMode=1
	subconsciousMouth.speakBlocking(unicode(lang_alert,'utf-8'))
	
	if errorType=="ArduinoNotConnected":
		errorSpoken=lang_ArduinoNotConnected+param

	if errorType=="BadMrlcommVersion":
		errorSpoken=lang_BadMrlcommVersion+param
		
	if errorType=="VoiceDownloaded":
		errorSpoken=lang_VoiceDownloaded
	
	if errorType=="MyvoiceType":
		errorSpoken=lang_MyvoiceType

	if errorType=="MyLanguage":
		errorSpoken=lang_MyLanguage
		
	if errorType=="MrlNeedUpdate":
		errorSpoken=lang_MrlNeedUpdate
		
	if errorType=="BAdrduinoChoosen":
		errorSpoken=lang_BAdrduinoChoosen+param
		
	if errorType=="ConfigParserProblem":
		errorSpoken=lang_ConfigParserProblem+param
		
	if errorType=="BadLanguagePack":
		errorSpoken=lang_BadLanguagePack
	
	subconsciousMouth.speakBlocking(unicode(errorSpoken,'utf-8'))
	
	print errorSpoken
		
