#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import re
import warnings


import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from IPython.display import display
from mpl_toolkits.basemap import Basemap
from wordcloud import WordCloud, STOPWORDS


from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize

matplotlib.style.use('ggplot')
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore")

get_ipython().run_line_magic('matplotlib', 'inline')

tweets = pd.read_csv('../input/tweets_all.csv', encoding = "ISO-8859-1")
tag =str(input("Please enter your hashtag/text:"))
def clean_input(tag):
    tag =tag.replace(" ","")
    if tag.startswith("#"):
        return tag[1:].lower()
    else:
        return tag.lower()
def return_all_hashtags(tweets, tag):
    all_hashtags=[]
    for tweet in tweets:
        for word in tweet.split():
            if word.startswith("#") and word.lower() != "#"+tag.lower():
                all_hashtags.append(word.lower())
    return all_hashtags
consumer_key= [Your consumer key]
consumer_secret= [Your consumer secret]
access_token= [Your access token]
access_token_secret= [Your access token secret]
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
import tweepy as tw

def get_hashtags(tag):
    search_tag=clean_input(tag)
    tweets = tw.Cursor(api.search,
                q=’#’+search_tag,
                lang=”en”).items(200)
    tweets_list=[] 
    for tweet in tweets:
        tweets_list.append(tweet.text)
    all_tags= return_all_hashtags(tweets_list, search_tag)
    frequency={} 
    for item in set(all_tags):
        frequency[item]=all_tags.count(item)
    return {k: v for k, v in sorted(frequency.items(), 
                key=lambda item: item[1], reverse= True)}
def generate_report(self, hashtag, api_data):
        """
        Generate Hashtag Report
        """

        search_timestamp = datetime.datetime.now()

        date = search_timestamp.strftime("%m%d%Y")

        search_filename = hashtag + "_" + date + ".html"


        hashtag_template = Template(
            filename='hashtag_search_result_template.html',
            input_encoding='utf-8',
            output_encoding='utf-8',
            encoding_errors='replace')

        try:

       
            with open(search_filename, 'wb+') as file_pointer:

                file_pointer.write(hashtag_template.render(
                    Search_String=hashtag,
                    Date=search_timestamp.strftime("%m/%d/%Y"),
                    Time=search_timestamp.strftime("%H:%M:%S"),
                    result_list=api_data))
                file_pointer.close()
                print("Hashtag Report Generated")

        except IOError:

            print("Error In Opening File For Writing Hashtag Report")
            raise Exception
all_tags = get_hashtags(tag)
for item in all_tags:
    print(item, all_tags[item])

