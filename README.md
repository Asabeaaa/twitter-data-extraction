# Twitter Data Extraction
## Project Overview
Created a script that downloads tweets data on a specific search topic (Endsars) using the tweepy standard search API. 
When this python script is run it makes a call to the Twitter Api using tweepy and returns a list of tweets with the word Endsars contained in it's text, converts the information we need which is stored in json objects into a dataframe and then stores the output in a csv file.

###### List of various functionality offered through Tweepy’s standard API:
1. post, retrieve and engage with tweets and timelines
2. post and receive direct messages 
3. manage and pull public account information
4. create and manage lists
5. follow, search and get users
6. retrieve trends

###### To gain credentials for tweepy
In order to receive credentials, you must apply to become a Twitter developer .(https://developer.twitter.com/en)
 
###### Libraries to import
- import tweepy
- import pandas as pd
- import datetime

###### Project was divided into 3 parts:
1. Passing credentials from Twitter Developers portal into python script
2. scrape_tweets() that has the following parameters: Search topic ,The number of tweets to download per request and returns a dataframe.
3. Save_results_as_csv() that has the following parameters: the dataframe from the above function and returns a csv file with the following naming format: tweets_downloaded_yymmdd_hhmmss.csv (where ‘yymmdd_hhmmss’ is the current 	timestamp) 

## Code and Resources used 
1. Twitter API docs: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets 
2. Tweepy docs: http://docs.tweepy.org/en/latest/api.html 

## Activities done
1. Passing credentials from Twitter Developers portal into python script
###### ![Capture10](https://user-images.githubusercontent.com/65185008/120348665-3b500800-c2b2-11eb-90f1-7af256e500b0.PNG)

2. scrape_tweets() function
- takes 2 parameters the text_query(EndSars), word used to filter tweets and the count which specifies the number of tweets you want to return from the search and coverts it into a dataframe after the needed information is taken from the returned tweets. This function returns the final dataframe created.
- The following attributes were gotten from the tweets extracted: 
-- Tweet text 
-- Tweet id 
-- Likes count 
-- Username 
-- Screenname 
-- Location 
-- Friends count 
-- Verification status 
-- Description 
-- Followers count

###### ![Capture11](https://user-images.githubusercontent.com/65185008/120349480-009a9f80-c2b3-11eb-8335-622ef469e8bd.PNG)
result is a json file that contains different objects that describe the tweets you have extracted, such as, tweet id, date tweeted,number of likes,all information related to the person who tweeted it,such as; the screen name, username,number of followers, etc. You can retrieve objects needed for your task

3. Save_results_as_csv() function
- takes one parameter which is the dataframe that was returned for the previous function and then converts it into a csv file

###### Output
## Save_results_as_csv() returns a csv file with the following naming format: tweets_downloaded_yymmdd_hhmmss.csv (where ‘yymmdd_hhmmss’ is the current 	timestamp) 
the current time stamp is generated automatically using datetime.datetime.now().strftime(time_format), where time_format is the specified format you want the date to be in ("%d-%m-%Y_%H-%M-%S")





