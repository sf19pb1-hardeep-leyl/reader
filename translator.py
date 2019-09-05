"""
translate.py
Loop through the lines of a text file downloaded from the Internet.
Convert each line from a sequence of bytes to a string of characters and translate them.
need to run pip install googletrans on BMCC Mac, or py -3 -m pip install googletrans
"""

# Prob doesnt work yet, couldnt test it at work because of firewalls
import sys
import urllib.request
from xgoogle.translate import Translator

translator = Translator()

language_code = """
Language Code
-------- ----
Afrikaans       af
Albanian        sq
Arabic  ar
Belarusian      be
Bulgarian       bg
Catalan         ca
Chinese Simplified      zh-CN
Chinese Traditional     zh-TW
Croatian        hr
Czech   cs
Danish  da
Dutch   nl
English         en
Estonian        et
Filipino        tl
Finnish         fi
French  fr
Galician        gl
German  de
Greek   el
Hebrew  iw
Hindi   hi
Hungarian       hu
Icelandic       is
Indonesian      id
Irish   ga
Italian         it
Japanese        ja
Korean  ko
Latvian         lv
Lithuanian      lt
Macedonian      mk
Malay   ms
Maltese         mt
Norwegian       no
Persian         fa
Polish  pl
Portuguese      pt
Romanian        ro
Russian         ru
Serbian         sr
Slovak  sk
Slovenian       sl
Spanish         es
Swahili         sw
Swedish         sv
Thai    th
Turkish         tr
Ukrainian       uk
Vietnamese      vi
Welsh   cy
Yiddish         yi
"""
print("We're going to translate a verse from Romeo and Juliet into another language that you select")

print(language_code)
language = input("Please select the language code: ")

url = "http://oit2.scps.nyu.edu/~meretzkm/python/string/romeo.txt"
lines = urllib.request.urlopen(url)

for line in lines:   #line is a sequence of bytes.
    s = line.decode("utf-8")
    translation = translate(s,lang_to=language)
    print(translation)           #s already ends with a newline.

lines.close()
sys.exit(0)
