from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0

def detect_language(text):
    try:
        language = detect(text)
        return language
    except LangDetectException as e:
        print(f"Error while detecting language: {e}")
        return None

text = "hello how are you"

language = detect_language(text)
if language is not None:
    print(f"The language of the text is: {language}")
else:
    print("Language detection failed.")
