def get_access_token():

    data = urllib.urlencode({
            'client_id' : client_id,
            'client_secret' : client_secret,
            'grant_type' : 'client_credentials',
            'scope' : 'http://api.microsofttranslator.com'
            })

    try:

        request = urllib2.Request('https://datamarket.accesscontrol.windows.net/v2/OAuth2-13')
        request.add_data(data) 

        response = urllib2.urlopen(request)
        response_data = json.loads(response.read())

        if response_data.has_key('access_token'):
            return response_data['access_token']

    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print datestring(), 'Could not connect to the server:', e.reason
        elif hasattr(e, 'code'):
            print datestring(), 'Server error: ', e.code
    except TypeError:
        print datestring(), 'Bad data from server'

supported_languages = { # as defined here: http://msdn.microsoft.com/en-us/library/hh456380.aspx
    'ar' : ' Arabic',
 #   'bs-Latn' : 'Bosnian (Latin)',
 #  'bg' : 'Bulgarian',
 #   'ca' : 'Catalan',
 #   'zh-CHS' : 'Chinese (Simplified)',
 #   'zh-CHT' : 'Chinese (Traditional)',
 #   'hr' : 'Croatian',
 #   'cs' : 'Czech',
    'da' : 'Danish',
    'nl' : 'Dutch',
    'en' : 'English',
 #  'et' : 'Estonian',
 #  'fi' : 'Finnish',
    'fr' : 'French',
    'de' : 'German',
    'el' : 'Greek',
 #  'ht' : 'Haitian Creole',
 #  'he' : 'Hebrew',
 #  'hi' : 'Hindi',
 #  'mww' : 'Hmong Daw',
 #  'hu' : 'Hungarian',
 #  'id' : 'Indonesian',
    'it' : 'Italian',
 #  'ja' : 'Japanese',
 #  'sw' : 'Kiswahili',
 #  'tlh' : 'Klingon',
 #  'tlh-Qaak' : 'Klingon (pIqaD)',
 #  'ko' : 'Korean',
 #  'lv' : 'Latvian',
 #  'lt' : 'Lithuanian',
 #  'ms' : 'Malay',
 #  'mt' : 'Maltese',
    'no' : 'Norwegian',
 #  'fa' : 'Persian',
 #  'pl' : 'Polish',
 #  'pt' : 'Portuguese',
 #  'otq' : 'Querétaro Otomi',
 #  'ro' : 'Romanian',
 #  'ru' : 'Russian',
 #  'sr-Cyrl' : 'Serbian (Cyrillic)',
 #  'sr-Latn' : 'Serbian (Latin)',
 #  'sk' : 'Slovak',
 #  'sl' : 'Slovenian',
    'es' : 'Spanish',
    'sv' : 'Swedish',
 #  'th' : 'Thai',
 #  'tr' : 'Turkish',
 #  'uk' : 'Ukrainian',
 #  'ur' : 'Urdu',
 #  'vi' : 'Vietnamese',
 #  'cy' : 'Welsh',
 #  'yua' : 'Yucatec Maya',
}

male_languages = { 
    'ar' : 'Nizar',
    'da' : 'Rasmus',
    'nl' : 'Jeroen',
    'en' : 'Ryan',
    'fr' : 'Antoine',
    'de' : 'Klaus',
    'el' : 'Dimitris',
    'it' : 'Vittorio',
    'no' : 'Olav',
    'es' : 'Antonio',
    'sv' : 'Emil',
}
en_languages = {
    'arab' : ' ar',
    'danish' : 'da',
    'dutch' : 'nl',
    'english' : 'en',
    'french' : 'fr',
    'german' : 'de',
    'greek' : 'el',
    'italian' : 'it',
    'norway' : 'no',
    'spanish' : 'es',
    'sweden' : 'sv',
}