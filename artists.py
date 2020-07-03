#!/usr/bin/env python3

#   A brief webscraping script to summarise/report on defined
#   elements on each Samling Artist profile page.
#   For further information, see the README.

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


page_url = "http://www.samling.org.uk/samling-artist-programme/artists/"
uClient = uReq(page_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
musicians = page_soup.find_all("h1", {"class": "artist__name"})

out_filename = "sap_artists.csv"
headers = "Name,URL,Voice-type/Instrument,SAP-Year,IMG \n"

f = open(out_filename, "w")
f.write(headers)

for musician in musicians:
    name = str(musician.text.strip())
    link = str(musician.a["href"])
    tClient = uReq(link)
    musician_html = tClient.read()
    tClient.close()
    musician_soup = soup(musician_html, "html.parser")
    head_text = musician_soup.h2.text
    if musician_soup.article.div.img is not None:
        IMG = "Yes"
    else:
        IMG = "No"
    f.write(
        name
        + ","
        + link
        + ","
        + head_text.replace(", Samling Artist Programme: ", ",")
        + ","
        + IMG
        + "\n"
    )

#   NB: The parsing/outputting of the head_text is a bit clunky, but
#   is advantageous as it highlights inconsistencies and typos.

f.close()
