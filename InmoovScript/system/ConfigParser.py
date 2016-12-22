# ##############################################################################
# 								CONFIGPARSER FILE
# ##############################################################################

BasicConfig = ConfigParser.ConfigParser()
BasicConfig.read(RuningFolder+'Inmoov.config')

ScriptType=BasicConfig.get('MAIN', 'ScriptType')
MyRightPort=BasicConfig.get('ARDUINO', 'MyRightPort')
MyLeftPort=BasicConfig.get('ARDUINO', 'MyLeftPort')

#TODO CONFIG FILE UPDATE WITHOUT DELETE USER SETTINGS