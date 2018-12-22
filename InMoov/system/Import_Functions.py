# -*- coding: utf-8 -*- 
def is_number(x):
  try:
    float(x)
    return True
  except:
    return False
    
def is_number_for_aiml(x):
  if is_number(x):
    return "nb"
  else:
    return "alpha"
    
def mathX(x,y):
  if is_number(x) and is_number(y):
    return int(float(x)*float(y))
  else:
    return 0
    
def mathPlus(x,y):
  if is_number(x) and is_number(y):
    return int(float(x)+float(y))
  else:
    return 0
    
def mathMinus(x,y):
  if is_number(x) and is_number(y):
    return int(float(x)-float(y))
  else:
    return 0
    
def mathDivide(x,y):
  if is_number(x) and is_number(y):
    return float(x)/float(y)
  else:
    return 0
    
def RemoveFile(file):
  try:
    os.remove(file)
  except:
    pass

def CheckIfRobotCanLaunchAPPS(Needs):
  for modules in Needs:
    if not modules:
      return 0
      break
  return 1
  
def Parse(utfdata):
  try:
    utfdata = urllib2.urlopen(utfdata).read()
    utfdata = utfdata.replace("&#039;", "'")
    utfdata = utfdata.decode( "utf8" )
  except:
    utfdata=''
    pass
  return utfdata
  
  
  
#this function usefull to calculate a maximum average
def maxAverage(list,howMany):
  sortedmaxAverage=sorted(list)
  maxAvg=[]
  if len(sortedmaxAverage)>0:
    for value in range(-1, -howMany, -1):
      maxAvg.append(sortedmaxAverage[value])
    return sum(maxAvg) / len(maxAvg)
  else:
    return 0
    
 
# beta fonction to pluralize or singularize words
def pluralize(word):
    for GRAMMAR_RULE in (_ail_word, _al_word, _au_word, _eil_word, _eu_word, _ou_word, _s_word, _x_word, _z_word,
            _default):
        plural = GRAMMAR_RULE(word)
        if plural:
            return plural



def _ail_word(word):
    if word.endswith("ail"):
        if word == "ail":
            return "aulx"
        elif word in ("bail", "corail", u"émail", "fermail", "soupirail", "travail", "vantail", "ventail", "vitrail"):
            return word[:-3] + "aux"
        return word + "s"

def _al_word(word):
    if word.endswith("al"):
        if word in (
            "bal", "carnaval", "chacal", "festival", u"récital", u"régal",
            "bancal", "fatal", "fractal", "final", "morfal", "natal", "naval",
            u"aéronaval",
            u"anténatal", u"néonatal", u"périnatal", u"postnatal", u"prénatal",
            "tonal", "atonal", "bitonal", "polytonal",
            "corral", "deal", "goal", "autogoal", "revival", "serial", "spiritual", "trial",
            "caracal", "chacal", "gavial", "gayal", "narval", "quetzal", "rorqual", "serval",
            "metical", "rial", "riyal", "ryal",
            "cantal", "emmental", "emmenthal",
            u"floréal", "germinal", "prairial",
            ):
            return word + "s"
        return word[:-2] + "aux"

def _au_word(word):
    if word.endswith("au"):
        if word in ("berimbau", "donau", "karbau", "landau", "pilau", "sarrau", "unau"):
            return word + "s"
        return word + "x"

def _eil_word(word):
    if word.endswith("eil"):
        return "vieux" if word == "vieil" else word + "s"

def _eu_word(word):
    if word.endswith("eu"):
        if word in ("bleu", u"émeu", "enfeu", "pneu", "rebeu"):
            return word + "s"
        return word + "x"

def _ou_word(word):
    if word.endswith("ou"):
        if word in ("bijou", "caillou", "chou", "genou", "hibou", "joujou", "pou"):
            return word + "x"
        return word + "s"

def _s_word(word):
    if word[-1] == "s":
        return word

def _x_word(word):
    if word[-1] == "x":
        return word
        
def _z_word(word):
    if word[-1] == "z":
        return word
 
def _default(word):
    return word + "s"

# fonction globale pour passer au singulier

def Singularize(word):
    for GRAMMAR_RULE in (_ail_word_sing, _ou_word_sing, _s_word_sing, _eu_word_sing, _default_sing):
        singular = GRAMMAR_RULE(word)
        if singular:
            return singular
      
def _ail_word_sing(word):
  if word.endswith("aux"):
    if word in ("baux", "coraux", u"émaux", "fermaux", "soupiraux", "travaux", "vantaux", "ventaux", "vitraux"):
      return word[:-3] + "ail"
    else:
      return word[:-3] + "al"
      
def _ou_word_sing(word):
    if word.endswith("oux"):
      if word in ("bijoux", "cailloux", "choux", "genoux", "hiboux", "joujoux", "poux"):
        return word[:-1]
      else:
        return word
      
def _s_word_sing(word):
  if word.endswith("s"):
    if word in (u"abcès", u"accès", "abus", "albatros", "anchois", "anglais", "autobus", "brebis", "carquois", "cas", "chas", "colis", "concours", "corps", "cours", u"cyprès", u"décès", "devis", "discours", "dos", "embarras", "engrais", "entrelacs", u"excès", u"fiançailles", "fois", "fonds", u"gâchis", "gars", "glas", "guet-apens", u"héros", "intrus", "jars", "jus", u"kermès", "lacis", "legs", "lilas", "marais", "matelas", u"mépris", "mets", "mois", "mors", "obus", "os", "palais", "paradis", "parcours", "pardessus", "pays", "plusieurs", "poids", "pois", "pouls", "printemps", "processus", u"progrès", "puits", "pus", "rabais", "radis", "recors", "recours", "refus", "relais", "remords", "remous", u"rhinocéros", "repas", "rubis", "sas", "secours", "souris", u"succès", "talus", "tapis", "taudis", "temps", "tiers", "univers", "velours", "verglas", "vernis", "virus", "accordailles", "affres", "aguets", "alentours", "ambages", "annales", "appointements", "archives", "armoiries", u"arrérages", "arrhes", "calendes", "cliques", "complies", u"condoléances", "confins", u"dépens", u"ébats", "entrailles", u"épousailles", "errements", "fiançailles", "frais", u"funérailles", "gens", "honoraires", "matines", "mœurs", u"obsèques", u"pénates", "pierreries", u"préparatifs", "relevailles", "rillettes", u"sévices", u"ténèbres", "thermes", "us", u"vêpres", "victuailles"):
      return word
    else:
      return word[:-1]
      
def _eu_word_sing(word):
  if word.endswith("eux"):
    if word=="yeux":
      return "oeil"
    else:
      return word[:-1]
      
def _default_sing(word):
  return word
      