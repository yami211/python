from typing import Optional, Tuple, Union
from googletrans import Translator, LANGUAGES

translator = Translator(service_urls=['translate.googleapis.com'])

def TransLate(text: str, scr: str, dest: str) -> str:

    if not text:
        return "Error: порожній текст"
    try:
        dest_code = CodeLang(dest)
        src_code = None if (scr is None or scr.lower() == 'auto') else CodeLang(scr)
        if dest_code is None:
            return f"Error: невідомий dest '{dest}'"
        res = translator.translate(text, src=src_code or 'auto', dest=dest_code)
        return res.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> Union[str, Tuple[str, float]]:
    try:
        detected = translator.detect(text)
        lang = detected.lang
        conf = getattr(detected, 'confidence', None)  
        if set == "lang":
            return lang
        if set == "confidence":
            return str(conf) if conf is not None else "None"
        # all
        return (lang, conf if conf is not None else 0.0)
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> Optional[str]:
    if not lang:
        return None
    lang_lower = lang.strip().lower()
    if lang_lower in LANGUAGES:
        return lang_lower
    for code, name in LANGUAGES.items():
        if name.lower() == lang_lower:
            return code
    for code, name in LANGUAGES.items():
        if lang_lower in name.lower() or name.lower() in lang_lower:
            return code
    return None

def LanguageList(out: str = "screen", text: Optional[str] = None) -> str:

    try:
        langs = sorted(LANGUAGES.items(), key=lambda x: x[0]) 
        header = f"{'Code':<8} {'Language':<30}"
        if text:
            header += f" {'Translation':<40}"
        lines = [header, "-" * len(header)]
        for code, name in langs:
            line = f"{code:<8} {name:<30}"
            if text:
                try:
                    tr = translator.translate(text, dest=code).text
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
            with open("language_list.txt", "w", encoding="utf-8") as f:
                f.write(out_text)
            return "Ok"
        else:
            return "Error: unknown out param"
    except Exception as e:
        return f"Error: {e}"