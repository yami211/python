import json
import os
import sys
import re
from texttrans import langdetect_deeptr as dtr   

CFG_FILE = "config.json"

def count_sentences(text: str) -> int:
    return max(0, len(re.findall(r'[.!?]+', text)))

def read_config(cfg_path: str):
    if not os.path.exists(cfg_path):
        raise FileNotFoundError(f"Config file {cfg_path} not found.")
    with open(cfg_path, "r", encoding="utf-8") as f:
        return json.load(f)

def process():
    cfg = read_config(CFG_FILE)
    infile = cfg.get("input_file")
    target_lang = cfg.get("target_lang")
    module_name = cfg.get("module", "deeptr_langdetect")  
    out = cfg.get("out", "screen")
    max_chars = cfg.get("max_chars", None)
    max_words = cfg.get("max_words", None)
    max_sentences = cfg.get("max_sentences", None)

    if not os.path.exists(infile):
        print(f"Error: input file {infile} not found.")
        return

    full_text = open(infile, "r", encoding="utf-8").read()
    size = os.path.getsize(infile)
    total_chars = len(full_text)
    total_words = len(full_text.split())
    total_sentences = count_sentences(full_text)
    try:
        lang, conf = dtr.LangDetect(full_text, set="all")
    except Exception:
        lang, conf = "unknown", 0.0

    print("File:", infile)
    print("Size (bytes):", size)
    print("Total chars:", total_chars)
    print("Total words:", total_words)
    print("Total sentences:", total_sentences)
    print("Detected language:", lang, f"(confidence {conf:.2f})")

    if module_name == "deeptr_langdetect":
        mod = dtr
    else:
        mod = dtr   

    read_chars = 0
    read_words = 0
    read_sentences = 0
    collected = []
    with open(infile, "r", encoding="utf-8") as f:
        for line in f:
            collected.append(line)
            read_chars += len(line)
            read_words += len(line.split())
            read_sentences += count_sentences(line)
            stop = False
            if max_chars and read_chars >= max_chars:
                stop = True
            if max_words and read_words >= max_words:
                stop = True
            if max_sentences and read_sentences >= max_sentences:
                stop = True
            if stop:
                break

    to_translate = "".join(collected).strip()
    if not to_translate:
        print("No text read for translation.")
        return

    translated = mod.TransLate(to_translate, "auto", target_lang) 
    if out == "screen":
        print("\n--- Translation result ---")
        print("Target language:", target_lang)
        print("Module used:", module_name)
        print(translated)
    elif out == "file":
        base, ext = os.path.splitext(infile)
        outname = f"{base}_{target_lang}{ext}"
        try:
            with open(outname, "w", encoding="utf-8") as wf:
                wf.write(translated)
            print("Ok")
        except Exception as e:
            print("Error writing output file:", e)
    else:
        print("Unknown output option in config.")

if __name__ == "__main__":   
    try:
        process()
    except Exception as e:
        print("Error:", e)
        sys.exit(1)