import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)  # Create an instant
language_translator.set_service_url(url)

# from pandas import json_normalize

# list_language=json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
# print(list_language)

def EnglishToFrench(englishText):
    
    translation_response = language_translator.translate(text=englishText, model_id='en-fr')
    frenchText=translation_response.get_result()
    return frenchText

def FrenchToEnglish(frenchText):
    
    translation_response = language_translator.translate(text=englishText, model_id='en-fr')
    frenchText=translation_response.get_result()
    return frenchText


englishText = "Hello World. I am Loc"
french_Text_Translate = EnglishToFrench(englishText)
print(french_Text_Translate['translations'][0]['translation'])



