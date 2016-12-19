# ##############################################################################
# 								CONFIGPARSER FILE
# ##############################################################################

BasicConfig = ConfigParser.ConfigParser()
BasicConfig.read(RuningFolder+'BasicConfig.ini')
ScriptType=BasicConfig.get('MAIN', 'ScriptType')
MyRightPort=BasicConfig.get('ARDUINO', 'MyRightPort')