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


OpenWeatherMap=Runtime.createAndStart("OpenWeatherMap", "OpenWeatherMap")
OpenWeatherMap.setApiKey(apikey)
try:
  OpenWeatherMap.setUnits(setUnits)
except:
  pass


def isTheSunShiny(townParam="town"):
  if townParam=="town" or townParam=="":townParam=town
  print townParam
  weather=OpenWeatherMap.fetchCurrentWeather(townParam)
  
  if weather:
    print weather[1]
    forecast=weather[3].decode("utf-8")
    
    print "SYSTEM METEO curtemperature " + str(int(round(float(weather[1])))) + " Town " + str(weather[2]) + " COMMENTAIRE " + str(forecast)
    chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(round(float(weather[1])))) + " Town " + str(weather[2]) + " COMMENTAIRE " + str(forecast))
  else:
    print "open weathermap error"
    chatBot.getResponse("SYSTEM openweathermapError")


def doITakeAnUmbrella(townParam="town",index):
  if townParam=="town" or townParam=="":townParam=town
  print index,townParam
  weather=OpenWeatherMap.fetchForecast(townParam,index)
  
  if weather:
    print weather[1]
    forecast=weather[3].decode("utf-8")
    
    print "SYSTEM METEO curtemperature " + str(int(round(float(weather[1])))) + " Town " + str(weather[2]) + " COMMENTAIRE " + str(forecast)
    chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(round(float(weather[1])))) + " Town " + str(weather[2]) + " COMMENTAIRE " + str(forecast))
  else:
    print "open weathermap error"
    chatBot.getResponse("SYSTEM openweathermapError")    
