

#!/usr/bin/python
from twitter import *
import random
import os
import json

from config import consumer_key, consumer_secret, access_key, access_secret

auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

if not os.path.exists('gastronomia.dump'):
    f = open('gastronomia.txt', 'r').read().split('\n\n')
    dump = open('gastronomia.dump', 'w+')
    json.dump([x.strip() for x in f if x.strip()], dump)
    dump.close()

dump = open('gastronomia.dump', 'r')
tweets = json.load(dump)
dump.close()
if not tweets:
    f = open('gastronomia.txt', 'r').read().split('\n\n')
    dump = open('gastronomia.dump', 'w+')
    tweets = [x.strip() for x in f if x.strip()]
    json.dump(tweets, dump)
    dump.close()
random.shuffle(tweets)
t = tweets.pop()
dump = open('gastronomia.dump', 'w+')
json.dump(tweets, dump)
dump.close()
twitter.statuses.update(status=t)
print("tweets left: ", len(tweets))
print (t)