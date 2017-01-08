# ##############################################################################
# 								CONFIGPARSER FILE
# ##############################################################################

#shared parse function
def CheckFileExist(File):
	global RobotIsErrorMode
	if not os.path.isfile(File+'.config'):
		shutil.move(File+'.config.default',File+'.config')
		print "config file created : ",File+'.config'

	
CheckFileExist(RuningFolder + 'Inmoov')
try:
	#basic config parse
	BasicConfig = ConfigParser.ConfigParser(allow_no_value = True)
	BasicConfig.read(RuningFolder+'Inmoov.config')

	# CONFIG FILE UPDATE ( if we add prameters and you have an old file )
	#if not BasicConfig.has_option('ARDUINO','MyNeopixelPort'):
	#	config= ConfigParser.RawConfigParser()
	#	config.read(RuningFolder+'Inmoov.config')
	#	config.set('ARDUINO','MyNeopixelPort',0)
	#	with open(RuningFolder+'Inmoov.config', 'wb') as configfile:
	#		config.write(configfile)

	# PARSE THE CONFIG FILE
	ScriptType=BasicConfig.get('MAIN', 'ScriptType')
	MyRightPort=BasicConfig.get('ARDUINO', 'MyRightPort')
	MyLeftPort=BasicConfig.get('ARDUINO', 'MyLeftPort')
	#read personnal config

	MyvoiceTTS=BasicConfig.get('TTS', 'MyvoiceTTS')
	MyLanguage=BasicConfig.get('TTS', 'MyLanguage').lower()
	MyvoiceType=BasicConfig.get('TTS', 'MyvoiceType')
	
	DEBUG=BasicConfig.getboolean('MAIN', 'debug')
	IsMute=BasicConfig.getboolean('VOCAL', 'IsMute')


except:
	
	print 'ConfigParserProblem'
	RobotIsErrorMode=1
	pass	
