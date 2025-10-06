from typing import Optional, Tuple, Union
from deep_translator import GoogleTranslator, DeeplTranslator, single_detection
from langdetect import detect_langs

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        target = dest
        tr = GoogleTranslator(source=scr if scr and scr != 'auto' else 'auto', target=target).translate(text)
        return tr
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> Union[str, Tuple[str, float]]:

    try:
        langs = detect_langs(text)
        best = langs[0]
        lang = best.lang
        conf = best.prob
        if set == "lang":
            return lang
        if set == "confidence":
            return str(conf)
        return (lang, conf)
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> Optional[str]:
    common = {
        'english': 'en', 'ukrainian': 'uk', 'russian': 'ru',
        'french': 'fr', 'german': 'de', 'spanish': 'es'
    }
    if not lang:
        return None
    l = lang.strip().lower()
    if len(l) <= 3:
        return l
    return common.get(l, None)

def LanguageList(out: str = "screen", text: Optional[str] = None) -> str:
    languages = {
        'en': 'english', 'uk': 'ukrainian', 'ru': 'russian',
        'fr': 'french', 'de': 'german', 'es': 'spanish'
    }
    try:
        header = f"{'Code':<8} {'Language':<20}"
        if text:
            header += f" {'Translation':<40}"
        lines = [header, "-" * len(header)]
        for code, name in languages.items():
            line = f"{code:<8} {name:<20}"
            if text:
                try:
                    tr = TransLate(text, 'auto', code)
                except Exception:
                    tr = "<err>"
                tr_short = (tr[:37] + "...") if len(tr) > 40 else tr
                line += f" {tr_short:<40}"
            lines.append(line)
        out_text = "\n".join(lines)
        if out == "screen":
            print(out_text)
            return "Ok"
        elif out == "file":
            with open("language_list_deeptr.txt", "w", encoding="utf-8") as f:
                f.write(out_text)
            return "Ok"
        else:
            return "Error: unknown out param"
    except Exception as e:
        return f"Error: {e}"