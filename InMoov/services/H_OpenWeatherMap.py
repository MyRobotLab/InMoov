# -- coding: utf-8 --
# ##############################################################################
#                 OPENWEATHERMAP FILE
# ##############################################################################


#parse config
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
setUnits=ThisServicePartConfig.get('MAIN', 'setUnits')
apikey=ThisServicePartConfig.get('MAIN', 'apikey')
town=ThisServicePartConfig.get('MAIN', 'town').replace('"',"")

openWeatherMap=Runtime.createAndStart("openWeatherMap", "OpenWeatherMap")
openWeatherMap.setKey(apikey)
openWeatherMap.setUnits(setUnits)

# forecast index 1 is next 3 hours , so 24 hours is 8
def isTheSunShiny(townParam="town",period=1):  
  if townParam=="town" or townParam=="":townParam=town
  openWeatherMap.setLocation(townParam)
  openWeatherMap.setPeriod(period)
  curtemperature=openWeatherMap.getDegrees()
  rawCode=openWeatherMap.getWeatherCode()
  if not rawCode==0:
    i01.chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(curtemperature)) + " Town " + str(townParam.split(',')[0] + " COMMENTAIRE " + str(rawCode)))
  else:
    i01.chatBot.getResponse("SYSTEM openweathermapError")