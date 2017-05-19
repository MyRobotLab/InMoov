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
town=ThisServicePartConfig.get('MAIN', 'town')


OpenWeatherMap=Runtime.createAndStart("OpenWeatherMap", "OpenWeatherMap")
OpenWeatherMap.setApiKey(apikey)
OpenWeatherMap.setUnits(setUnits)

  
global isOpenWeatherMapOk
isOpenWeatherMapOk=0

def getRawWeather(townParam):
  global isOpenWeatherMapOk
  r=["bad weather api key","1000","bad weather api key","1000"]
  try:
  	r=OpenWeatherMap.fetchRaw(townParam)
  	isOpenWeatherMapOk=1
  except:
  	pass
  return r
  
def isTheSunShiny(townParam=town):
  weather=getRawWeather(townParam)
  
  if weather[1]!=1000 and isChatbotActivated:
    todayforecast=weather[3].decode("utf-8")
    
    print "SYSTEM METEO curtemperature " + str(int(round(float(weather[1])))) + " Town " + str(weather[2]) + " COMMENTAIRE " + str(todayforecast)
    chatBot.getResponse("SYSTEM METEO curtemperature " + str(int(round(float(weather[1])))) + " Town " + str(weather[2]) + " COMMENTAIRE " + str(todayforecast))
  
  
  