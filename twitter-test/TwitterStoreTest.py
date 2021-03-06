__author__ = 'marc'

import twitter  # Tell Python to use the twitter package

lines = [line.strip() for line in open('twitter.cfg')]

CONSUMER_KEY        = lines[0]
CONSUMER_SECRET     = lines[1]
OAUTH_TOKEN         = lines[2]
OAUTH_TOKEN_SECRET  = lines[3]

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

q = '#jesuischarlie' # XXX: Set this variable to a trending topic, or anything else you like.
count = 100 # number of results to retrieve

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets for more info

search_results = twitter_api.search.tweets(q=q, count=count) # search for your query 'q' 100 times
statuses = search_results['statuses'] # extract the tweets found

status_texts = [status['text'] for status in statuses]

screen_names = [user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]

hashtags = [hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags']]

# Compute a collection of all words from all tweets
words = [w for t in status_texts for w in t.split()] #split the string on the empty spaces

from collections import Counter
for item in [words, screen_names, hashtags]:
    c = Counter(item)

import cPickle
f = open("myData.pickle", "wb") # create a file handle for writing (w) in binary mode (b) named myData.pickle,
cPickle.dump(words, f) # write the contents of list 'words' to file 'f'
f.close() #  clean up after yourself
