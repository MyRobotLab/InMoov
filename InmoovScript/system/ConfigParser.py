# ##############################################################################
# 								CONFIGPARSER FILE
# ##############################################################################

#shared parse function
def CheckConfigFileExist(File):
	if not os.path.isfile(File+'.config'):
		shutil.move(File+'.config.default',File+'.config')
		print "config file created : ",File+'.config'
		
CheckConfigFileExist(RuningFolder + 'Inmoov')
	
#basic config parse
BasicConfig = ConfigParser.ConfigParser()
BasicConfig.read(RuningFolder+'Inmoov.config')

ScriptType=BasicConfig.get('MAIN', 'ScriptType')
MyRightPort=BasicConfig.get('ARDUINO', 'MyRightPort')
MyLeftPort=BasicConfig.get('ARDUINO', 'MyLeftPort')

#TODO CONFIG FILE UPDATE