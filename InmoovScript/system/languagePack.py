# language pack

languagePack=MyLanguage
languagePackLoaded=1

# we load default english language pack

for root, subdirs, files in os.walk(RuningFolder+'languagePack/en'):
	for name in files:
		if name.split(".")[-1] == "lang":
			#if chatbot loaded we do not load ear.addcommands
			if "ear.addCommand" in root and EarInterpretEngine=="chatbot":
				print "info : ommit ear.addCommand directory from language pack because chatbot use"
				print " >> ",os.path.join(root, name)
			else:
				execfile(os.path.join(root, name).encode('utf8'))
				if DEBUG==1:
					print "debug languagePack : ",os.path.join(root, name)

			
# we try to load user system language pack
	
if (os.path.isdir(RuningFolder+'languagePack/'+languagePack)):
	try:
		for root, subdirs, files in os.walk(RuningFolder+'languagePack/'+languagePack):
				for name in files:
					if name.split(".")[-1] == "lang":
						if "ear.addCommand" in root and EarInterpretEngine=="chatbot":
							print "info : ommit user ear.addCommand directory from language pack because chatbot use"
							print " >> ",os.path.join(root, name)
						else:
							execfile(os.path.join(root, name).encode('utf8'))
							if DEBUG==1:
								print "debug user languagePack : ",os.path.join(root, name)
		
	except:
		languagePackLoaded=0
		pass
else:
	languagePackLoaded=0