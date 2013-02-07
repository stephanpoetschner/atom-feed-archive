# Abstract

Tool to export data from wordpress blogs.

Developed when I needed a tool to archive the data from my friends travel' blogs.

## Manual steps needed

* Add Feed (e.g. http://danuel.wordpress.com/feed/) to Google Reader Account
* Download an Atom-Feed file from your Google Reader Account (including all entries)
  e.g. http://www.google.com/reader/atom/feed/http%3A%2F%2Fdanuel.wordpress.com%2Ffeed%2F?n=1000
  Save the file to "feed.atom"
* Install all requirements by using pip
  `pip install -r requirements.txt`
* Run script
  `python archive_atom.py`
