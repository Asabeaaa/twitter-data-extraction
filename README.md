# twitter-data-extraction
This is a script that downloads tweets data on a specific search topic (Endsars) using the tweepy standard search API. 

#Description
When this python script is run it makes a call to the Twitter Api using tweepy and returns a list of tweets with the word Endsars contained in it's text, converts the information we need which is stored in json objects into a dataframe and then stores the output in a csv file.

#Required dependencies to install
Pip install Tweepy

#Libraries to import
import tweepy
import pandas as pd
import datetime

#List of various functionality offered through Tweepy’s standard API:
post, retrieve and engage with tweets and timelines
post and receive direct messages 
manage and pull public account information
create and manage lists
follow, search and get users
retrieve trends

#To gain credentials for tweepy
In order to receive credentials, you must apply to become a Twitter developer .(https://developer.twitter.com/en)

#Project was divided into 3 parts:
Getting credentials from Twitter Developers portal
scrape_tweets() that has the following parameters: Search topic ,The number of tweets to download per request and returns a dataframe.
Save_results_as_csv() that has the following parameters: the dataframe from the above function and returns a csv file with the following naming format: tweets_downloaded_yymmdd_hhmmss.csv (where ‘yymmdd_hhmmss’ is the current 	timestamp)  

The following attributes were gotten from the tweets extracted: 
Tweet text 
Tweet id 
Likes count 
Username 
Screenname 
Location 
Friends count 
Verification status 
Description 
Followers count









