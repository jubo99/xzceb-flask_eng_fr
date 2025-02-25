"""This module translates text."""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """Translate from English to French"""
    #write code here
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translate from French to English"""
    #write code here
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
