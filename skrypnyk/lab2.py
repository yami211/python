from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory, detect_langs

# Для стабільного визначення мови
DetectorFactory.seed = 0

language_dict = {
    "english": "en",
    "ukrainian": "uk",
    "french": "fr",
    "german": "de",
    "spanish": "es",
    "russian": "ru"
}

def TransLate(text, lang):
    try:
        target_code = CodeLang(lang)
        translated = GoogleTranslator(source='auto', target=target_code).translate(text)
        return translated
    except Exception as e:
        return f"Error: {e}"

# Надійна функція визначення мови
def LangDetect(txt):
    try:
        lang_code = detect(txt)            # визначає мову, наприклад 'uk'
        confidence = max([p.prob for p in detect_langs(txt)])  # оцінка впевненості
        return lang_code, confidence
    except Exception:
        return None, None

def CodeLang(lang):
    lang = lang.lower()
    if lang in language_dict:  # назва мови -> код
        return language_dict[lang]
    elif lang in language_dict.values():  # код -> код
        return lang
    else:
        raise ValueError(f"Unknown language: {lang}")

if __name__ == "__main__":
    text = input("Введіть текст для перекладу: ")
    target_lang = input("Введіть мову перекладу (назва або код): ")

    translated = TransLate(text, target_lang)
    print("Переклад:", translated)

    lang_code, confidence = LangDetect(text)
    if lang_code:
        print(f"Визначена мова: {lang_code} (точність: {confidence:.2f})")
    else:
        print("Не вдалося визначити мову тексту")
