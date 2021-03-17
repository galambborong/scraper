# Samling Artists web scraper

## Update!

This was created as a time-saving solution when I worked at Samling Institute for Young Artists, which I left in December 2020. They have since launched a new website, so this script is now redundant. The last archived version of the site this script was designed to work with is [here](https://web.archive.org/web/20201202054649/http://www.samling.org.uk/samling-artist-programme/artists/).

## Main README contents

This brief webscraper loops through the unique URLs of every Samling Artist and reports defined elements into a csv file.

Run as a Python script, either by typing:

`$ ./artists.py` or `$ python artists.py`

Allow up to ~15 minutes for a complete scrape, though it will typically run much quicker than this. This script does not raise exceptions. For dependencies, see requirements.txt. 

### Current behaviour

The scraper reads <http://www.samling.org.uk/samling-artist-programme/artists/> for a list of all Samling Artists. From this, it extracts the artist's name and the URL of their local profile page. It then loops through each URL and reads the h2/sub-heading text which should conform to a set pattern: <VoiceType, Samling Artist Programme: Year>. It then checks for the presence of an image. Finally, it checks for the presence of a quote and, if present, saves this.  

This data is then appended to a csv file in the current working directory, reporting six headers: Name, URL, Voice-type/Instrument, SAP-Year, IMG, Quote.

#### Useful side effects

If the sub-header text does not match the pattern above, the scraper continues but the inconsistency is easily identified by the incorrect presence of the string 'Samling Artist Programme:' (or similar) and the 'IMG' response will be in the wrong column. 

### Recent changes

The inclusion of the quote scraping is new. It currently converts all commas from ',' to '[comma]' within the quote, so the csv output is not troubled. This can be overcome better (to allow commas within the quote strings), and will likely be revised. 
