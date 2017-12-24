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


# forecast index 1 is now to next 3 hours , so 24 hours is 8
def isTheSunShiny(townParam="town",period=1):
  OpenWeatherMap.setUnits(setUnits)
  if townParam=="town" or townParam=="":townParam=town
  print period,townParam
  weather=OpenWeatherMap.fetchForecast(townParam,period)
  
  if weather:
    print weather[1]
    forecast=weather[3].decode("utf-8")
    
    print "SYSTEM METEO curtemperature " + str(int(round(float(weather[1])))) + " Town " + str(weather[2]).split(',')[0] + " COMMENTAIRE " + str(forecast)
    chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(round(float(weather[1])))) + " Town " + str(weather[2]).split(',')[0] + " COMMENTAIRE " + str(forecast))
  else:
    print "open weathermap error"
    chatBot.getResponse("SYSTEM openweathermapError")