from googletrans import Translator


translator = Translator()

language_dict = {
    "english": "en",
    "ukrainian": "uk",
    "french": "fr",
    "german": "de",
    "spanish": "es"
}

# 1. Функція перекладу
def TransLate(text, lang):
    try:
        target_code = CodeLang(lang)
        translated = translator.translate(text, dest=target_code)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

# 2. Функція визначення мови
def LangDetect(txt):
    try:
        detected = translator.detect(txt)
        return detected.lang, detected.confidence
    except Exception as e:
        return None, None

# 3. Функція конвертації мови та коду
def CodeLang(lang):
    lang = lang.lower()
    if lang in language_dict:  # назва мови -> код
        return language_dict[lang]
    elif lang in language_dict.values():  # код 
        return lang
    else:
        raise ValueError(f"Unknown language: {lang}")

# 4. Головна програма
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
