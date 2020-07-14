#!/usr/bin/env python3

"""
This is a brief webscraping script to summarise/report on
defined elements on each Samling Artist profile page.

For further information, see the README.
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


URL = "http://www.samling.org.uk/samling-artist-programme/artists/"
HEADERS = "Name,URL,Voice-type/Instrument,SAP-Year,IMG,Quote\n"
OUT_FILENAME = "sap_artists.csv"

uClient = uReq(URL)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
musicians = page_soup.find_all("h1", {"class": "artist__name"})


f = open(OUT_FILENAME, "w", encoding="utf-8")
f.write(HEADERS)

for musician in musicians:
    NAME = str(musician.text.strip())
    LINK = str(musician.a["href"])
    tClient = uReq(LINK)
    musician_html = tClient.read()
    tClient.close()
    musician_soup = soup(musician_html, "html.parser")
    HEAD_TEXT = musician_soup.h2.text
    if musician_soup.article.div.img is not None:
        IMG = "Yes"
    else:
        IMG = "No"
    if musician_soup.div.blockquote is not None:
        QUOTE = str(musician_soup.div.blockquote.text)
    else:
        QUOTE = "No"
    f.write(
        NAME
        + ","
        + LINK
        + ","
        + HEAD_TEXT.replace(", Samling Artist Programme: ", ",")
        + ","
        + IMG
        + ","
        + QUOTE.replace(",", "[comma]")
        + "\n"
    )
f.close()
