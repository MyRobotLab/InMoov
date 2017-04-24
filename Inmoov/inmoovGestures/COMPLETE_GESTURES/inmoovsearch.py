def inmoovsearch(search):
  search = search.replace(" ", "+")  
  BareBonesBrowserLaunch.openURL("https://www.google.fr/search?q=" + str(search))
  True