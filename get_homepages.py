import pandas
import requests
import re
import itertools
from datetime import datetime
master_csv = 'https://docs.google.com/spreadsheet/pub?key=0An9Q5Mkz4lG7dGt6ZTNZLU03cnZRMkQtMkdaZ1lhd1E&single=true&gid=0&output=csv'
d = pandas.read_csv(master_csv)
unix_time = datetime.now().strftime("%s")

for u in d['site_url']:
  print "Scraping", u
  fname = re.sub("http://|/", "", u)
  f = open("homepages/" + fname + unix_time + ".html", "w")
  html = requests.get(u).text
  f.write(html.encode('utf-8'))
  f.close()

def
