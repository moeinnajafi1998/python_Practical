from googletrans import Translator

def translate_persian_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='fa', dest='en')
    return translation.text

def translate_english_to_persian(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='fa')
    return translation.text

# Example usage:
persian_text = "سلام، چطوری؟"
english_text = "Hello, how are you?"

translated_to_english = translate_persian_to_english(persian_text)
translated_to_persian = translate_english_to_persian(english_text)

print("Persian to English:", translated_to_english)
print("English to Persian:", translated_to_persian)
