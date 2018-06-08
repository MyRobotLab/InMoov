# ##############################################################################
#                 WEBGUI SERVICE
# ##############################################################################

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')

isWebGuiActivated=ThisServicePartConfig.get('MAIN', 'isWebGuiActivated')
if isWebGuiActivated:
  # Start the webgui service without starting the browser
  # As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
  # webgui = Runtime.createAndStart("webgui","WebGui")
  webgui = Runtime.create("webgui","WebGui")
  webgui.autoStartBrowser(False)
  webgui.startService()