# Obligatory README

This brief webscraper loops through the unique URLs of every Samling Artist and reports defined elements into a csv file.

Run as a Python script, either by typing:

```$ ./artists.py```

or

```$ python artists.py```

Allow up to ~15 minutes for a complete scrape, though it will typically run much quicker than this. This script does not raise exceptions. For dependencies, see requirements.txt. 

### Current behaviour

The scraper reads <http://www.samling.org.uk/samling-artist-programme/artists/> for a list of all Samling Artists. From this, it extracts the artist's name and the URL of their local profile page. It then loops through each URL and reads the h2/sub-heading text which should conform to a set pattern: <VoiceType, Samling Artist Programme: Year>. It then checks for the presence of an image. 

This data is then appended to a csv file in the current working directory, reporting five headers: Name, URL, Voice-type/Instrument, SAP-Year, IMG.

#### Useful side effects

If the sub-header text does not match the pattern above, the scraper continues but the inconsistency is easily identified by the incorrect presence of the string 'Samling Artist Programme:' (or similar) and the 'IMG' response will be in the wrong column. 

### Possible future adaption

This will likely extend to report the presence of both personal URLs and the URLs of an agent. It should also be possible to report the presence of blockquotations and custom biographies. 

Once fully trialled, this will be compiled into a .exe file for wider use.
