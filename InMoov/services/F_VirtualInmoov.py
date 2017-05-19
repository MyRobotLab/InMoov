# ##############################################################################
#                 VIRTUAL INMOOV SERVICE
# ##############################################################################
global virtualInmoovActivated
virtualInmoovActivated=False
if ScriptType=="Virtual" or virtualInmoovAlwaysActivated:
  if os.path.isdir(RuningFolder+'/jm3') and runtime.is64bit:
    global virtualInmoovActivated
    virtualInmoovActivated=True
  else:
    errorSpokenFunc("lang_VinmooovNoWorky")


#virtual inmoov
i01.VinmoovMonitorActivated=1
#i01.VinmoovFullScreen=0
#i01.VinmoovBackGroundColor="Grey"
#i01.VinmoovWidth=800
