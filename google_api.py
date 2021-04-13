import googletrans
from googletrans import Translator







translator = Translator()

def translate_from(language,msg):
    return(translator.translate(msg,source = language,out = 'en').text)



