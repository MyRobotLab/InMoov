wdf=Runtime.createAndStart("wdf", "WikiDataFetcher")
if MyLanguage=="fr":
   #WikiFile="BDD/WIKI_prop.txt"
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   #WikiFile="BDD/WIKI_propEN.txt"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")
