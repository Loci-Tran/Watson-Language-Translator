""" translator file with 2 function 1. english_to_french 2. FrenchToEnglish"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT='2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION_LT,
    authenticator=authenticator)  # Create an instant
language_translator.set_service_url(url)

def english_to_french(english_text):
    """"Translator english -> french"""
    translation_response = language_translator.translate(text=english_text,model_id='en-fr')
    french_text=translation_response.get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """"Translator french -> english"""
    translation_response = language_translator.translate(text=french_text,model_id='fr-en')
    english_text=translation_response.get_result()
    return english_text['translations'][0]['translation']


ENGLISH_TEXT = "Hello"
FRENCH_TEXT = english_to_french(ENGLISH_TEXT)
print(FRENCH_TEXT)



