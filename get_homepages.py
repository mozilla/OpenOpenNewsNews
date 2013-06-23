import pandas
import requests
import re
import urllib
import itertools
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup
from datetime import datetime
from itertools import groupby

master_csv = 'https://docs.google.com/spreadsheet/pub?key=0An9Q5Mkz4lG7dGt6ZTNZLU03cnZRMkQtMkdaZ1lhd1E&output=csv'
d = pandas.read_csv(master_csv)
time = datetime.now().strftime("%s")
data = []
for i in d.index:
  url = d['site_url'][i]
  regex = d['site_regex'][i]
  news_org = d['site_name'][i]
  soup = BeautifulSoup(requests.get(url).text)
  links = [urljoin(url, re.sub(url, "", a['href'].encode('utf-8'))) for a in soup.findAll('a',href=True)]
  articles = [l for l in links if re.match(regex, l)]
  articles = [a for a,_ in groupby(articles)]
  print "parsed %d links from %s" % (len(articles), news_org)
  org_data = {
    'news_org': news_org,
    'time': time,
    'regex': regex,
    'articles': articles
  }
  data.append(org_data)

data = [d for d in data if len(d['articles'])>0]

def detect_articles(org_data):
  print "updating data for %s" % org_data['news_org']
  org_data['html'] = []
  org_data['text'] = []
  org_data['title'] = []
  article_urls = org_data['articles']
  for i, url in enumerate(article_urls):
    print "finding article for %s" % url
    org_data['html'].append(requests.get(url).text)
    api_url = "http://boilerpipe-web.appspot.com/extract?url=" + urllib.quote_plus(url) + "&extractor=ArticleExtractor&output=json"
    bp = requests.get(api_url).json
    if bp['status']=="success":
      org_data['title'].append(bp['response']['title'])
      org_data['text'].append(bp['response']['content'])
    else:
      org_data['title'].append(None)
      org_data['text'].append(None)
  return org_data


new_data = [detect_articles(d) for d in data]
new_data
with open('data.txt', 'w') as f:
  json.dump(new_data[0], f)


'http://www.nytimes.com/')
soup = BeautifulSoup(r.text)

url_encoded_links = [urllib.]

links = [a['href'] for a in soup.findAll('a',href=True)]
[urllib.urlencode(l) for l in links if l!="\\#" or l!="" or l is not None]




for i in d.index:
  d['site_url']
  soup = BeautifulSoup(requests.get("http://www.nytimes.com").text)

for u in d['site_url']:
  print "Scraping", u
  html = requests.get(u).text
  f.write(html.encode('utf-8'))
  f.close()

def detect_article(url):
  ROOT_URL = "http://boilerpipe-web.appspot.com/extract?url="


