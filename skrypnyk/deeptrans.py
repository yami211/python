from texttrans import langdetect_deeptr as d3

if __name__ == "__main__":
    sample = "Bonjour, comment ça va?"
    print("LangDetect (all):", d3.LangDetect(sample, "all"))
    print("Translate to en:", d3.TransLate(sample, "auto", "en"))
    print("CodeLang('french') ->", d3.CodeLang("french"))
    d3.LanguageList("screen", sample)