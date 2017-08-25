# ##############################################################################
#                 VIRTUAL INMOOV SERVICE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

virtualInmoovAlwaysActivated=ThisServicePartConfig.getboolean('MAIN', 'virtualInmoovAlwaysActivated')
VinmoovMonitorActivated=ThisServicePartConfig.getboolean('MAIN', 'VinmoovMonitorActivated')

global virtualInmoovActivated
virtualInmoovActivated=False
if ScriptType=="Virtual" or virtualInmoovAlwaysActivated:
  if os.path.isdir(RuningFolder+'/jm3') and runtime.is64bit:
    global virtualInmoovActivated
    virtualInmoovActivated=True
  else:
    errorSpokenFunc("lang_VinmooovNoWorky")


#virtual inmoov
i01.VinmoovMonitorActivated=VinmoovMonitorActivated
#i01.VinmoovFullScreen=0
#i01.VinmoovBackGroundColor="Grey"
#i01.VinmoovWidth=800
