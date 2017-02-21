# -*- coding: utf-8 -*- 

# ##############################################################################
# 								WikiDataFetcher SERVICE FILE
# ##############################################################################

#script based on beetlejuice work and service
#sorry I will translate comments soon
#TODO : english chatbot integration

wdf=Runtime.createAndStart("wdf", "WikiDataFetcher")
if MyLanguage=="fr":
   #WikiFile="BDD/WIKI_prop.txt"
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   #WikiFile="BDD/WIKI_propEN.txt"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")
   
# ##############################################################################
# 								functions called by the chatbot
# ##############################################################################
if EarInterpretEngine=="chatbot":
	chatBot.setPredicate("default","particule","")
	chatBot.setPredicate("default","courant","")
def askWiki(particule,query,question,ReturnOk,ReturnNok): # retourne la description du sujet (query)
	#Light(1,0,0)
	if query!="":
		if particule!="":
			query=particule+" "+query
		query = unicode(query,'utf-8')# on force le format de police UTF-8 pour prendre en charge les accents
		if query[1]== "\'" : # Si le sujet contient un apostrophe , on efface tout ce qui est avant ! ( "l'ete" -> "ete")
			query2 = query[2:len(query)]
			query = query2
		print query # petit affichage de contrôle dans la console python ..
		
		
		start = wdf.grabStart(query).lower() # on garde que le determinant ( je ne sais plus pourquoi j'ai eu besoin de ca, mais la fonction existe ...)
		# coucou fred je vais m en servir en tous cas :) bon a terme faudra un autre dico pour detecter le feminin/masculin du premier mot du retour wiki
		
		WeCutTheFirstWord=0 #on enleve le/la/les etc... uniqument si présent
		retour = " c'est un, ou une, "
		if start=="du":
			start="le"
			retour=" c'est un, ou une, "
			WeCutTheFirstWord=1
		if start=="le":
			retour=" c'est un, ou une, "
			WeCutTheFirstWord=1
		if start=="l":
			retour=" c'est un, ou une, "
			WeCutTheFirstWord=1
		if start=="la":
			retour=" c'est un, ou une, "
			WeCutTheFirstWord=1
		if start=="une":
			retour=" c'est un, ou une, "
			WeCutTheFirstWord=1
		if start=="un":
			retour=" c'est un, ou une, "
			WeCutTheFirstWord=1
		if start=="des":
			start="les"
			retour=" ce sont des "
			WeCutTheFirstWord=1
		if start=="les":
			retour=" ce sont des "
			WeCutTheFirstWord=1

		if WeCutTheFirstWord==1:
			word = wdf.cutStart(query) # on enleve le derminant ("le chat" -> "chat")	
		else:
			word=query
		wordSingular = word=Singularize(word) # on met au singulier pour double test
		print word
		wikiAnswer = wdf.getDescription(word) # recupere la description sur wikidata

		answer = ( query + retour + wikiAnswer)
		
		print unicode(wikiAnswer[-9:],'utf-8')
		if (wikiAnswer == "Not Found !") or (unicode(wikiAnswer[-9:],'utf-8') == u"Wikimedia") or (unicode(wikiAnswer[-9:],'utf-8') == u"Wikimédia"): 
			wikiAnswer = wdf.getDescription(wordSingular)
		if (wikiAnswer == "Not Found !") or (unicode(wikiAnswer[-9:],'utf-8') == u"Wikimedia") or (unicode(wikiAnswer[-9:],'utf-8') == u"Wikimédia"): # bon on a toujours pas trouvé, prochaine etape a dev un dico de synonymes
			chatBot.getResponse(ReturnNok)
		else:
			chatBot.getResponse(ReturnOk + answer)
		chatBot.setPredicate("default","particule","")
	else:
		chatBot.getResponse(ReturnNok)

