def inmoovsearch(search):
  search = search.replace(" ", "+")  
  BareBonesBrowserLaunch.openURL("https://www.google.fr/search?q=" + str(search))
  #BareBonesBrowserLaunch.openURL("https://www.google.ru/search?q=" + str(search))
  True