from texttrans import gtrans4 as g4

if __name__ == "__main__":
    sample = "Hello world. This is a test."
    print("LangDetect (all):", g4.LangDetect(sample, "all"))
    print("Translate to uk:", g4.TransLate(sample, "auto", "uk"))
    print("CodeLang('ukrainian') ->", g4.CodeLang("ukrainian"))
    g4.LanguageList("screen", sample)