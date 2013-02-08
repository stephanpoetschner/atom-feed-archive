#!/usr/bin/env python
# coding: utf-8
from BeautifulSoup import BeautifulSoup
import HTMLParser
from os.path import basename

from django.template.defaultfilters import slugify
import requests

parser = HTMLParser.HTMLParser()
soup = BeautifulSoup(open('feed.atom'))
entries = soup.findAll('entry')

articles = []

for entry in entries:
    article = {
        'title': entry.title.text.encode('utf-8'),
        'published': entry.published.text.encode('utf-8'),
        'description': parser.unescape(entry.content.text).encode('utf-8')
    }
    links = map(lambda y: dict(y.attrs).get('href', ''),
        filter(
            lambda x: 'rel' not in dict(x.attrs) or dict(x.attrs)['rel'] != 'nofollow',
            BeautifulSoup(article['description']).findAll('a')
        )
    )
    article['links'] = links
    articles.append(article)

for article in articles:
    filename = slugify(article['title'])
    f = open('content/%s.txt' % filename, 'w')
    f.write(article['title'] + '\n')
    f.write(article['published'] + '\n')
    f.write('###\n')
    f.write(article['description'] + '\n')
    f.close()

    for link in article['links']:
        response = requests.get(link)
        filename = basename(link)
        if filename:
            f = open('media/%s' % filename, 'wb')
            f.write(response.content)
            f.close()
