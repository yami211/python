from texttrans import gtrans3 as g3

if __name__ == "__main__":
    sample = "Hello world. This is a test."
    print("LangDetect (all):", g3.LangDetect(sample, "all"))
    print("Translate to uk:", g3.TransLate(sample, "auto", "uk"))
    print("CodeLang('ukrainian') ->", g3.CodeLang("ukrainian"))
    g3.LanguageList("screen", sample)