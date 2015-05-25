# Not to stabby
#
# To determine the likelyhood of you being stabbed at a local bar.
#    by generating a "stabbyness rating"
# How?
#   Yelp API, Review web scraping.
#   Look for any suspect keywords in yelp reviews. Such as:
#       stab, foright, dark, dingy, dirty, sketchy, dive, blood
#

import urllib2
from yelpapi import YelpAPI
from scrapy import Spider, Item, Field
from scrapy.selector import Selector
import sys

from yelp_creds import consumer, secret, token, token_secret

stabby_terms = ['dark', 'dingy', 'dirty', 'dank', 'scared', 'blood', 'health inspector', 'disgusting', 'disturbing', 'rude', 'grungy', 'creep', 'clingy', 'moist', 'nightmare', 'gross', 'terrible', 'stink', 'pungent', ]

ten_point_terms = [' mold', 'urine', ' pee', 'vomit', 'mucus', ' feces', 'shiv', ' murder', 'death', 'police', 'bugs', 'cockroach', 'shank']


yelp = YelpAPI(consumer_key=consumer, consumer_secret=secret,
                    token=token, token_secret=token_secret)

if sys.argv[1]:
    bar = sys.argv[1]
else:
    print 'No search found'
    sys.exit()
    # return
try:
    location = sys.argv[2]
except:
    location = 'Edmonton, AB'

# print sys.argv
results = yelp.search_query(term=bar, location=location, category='Bar')
# results = ['1','2']
# Fat Baby, New York - 30
# lit lounge, New York - 40


for b in results['businesses']:
    # http://yelp.com/b['id']
    # yp = YelpSpider(start_urls=['https://yelp.com/%s' % (b['id'],)])
    response = urllib2.urlopen("http://yelp.com/biz/%s?sort_by=rating_asc" % (b['id'],), timeout=5)
    html = response.read()
    html = html.lower().split()
    one_scores = sum(stab in h for h in html for stab in stabby_terms)
    ten_scores = sum(stab in h for h in html for stab in ten_point_terms) * 10
    score = one_scores + ten_scores
    print "%s's Stabby Score: %s " % (b['id'], score, )
    # print yp

    # break

