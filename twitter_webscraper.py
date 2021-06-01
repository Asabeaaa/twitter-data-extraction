import tweepy
import pandas as pd
import datetime

consumer_key = "XXXXXX"
consumer_secret = "XXXXXX"
access_token = "XXXXXX"
access_token_secret = "XXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


class Twitter_etl:
    tweets= []

    def scrape_tweets(self,text_query,count):
        
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search,q=text_query).items(count)
       
    
        # Pulling information from tweets iterable object
        tweets_list = [[tweet.id,tweet.text,tweet.user.name,tweet.user.screen_name,tweet.user.location,tweet.user.description,tweet.created_at,tweet.user.verified,tweet.user.favourites_count,tweet.user.followers_count,tweet.user.friends_count] for tweet in tweets]

        # Creation of dataframe from tweets list
        # Add or remove columns as you remove tweet information
        tweets_df = pd.DataFrame(tweets_list,columns=['tweetId', 'Tweet','Username','screenName','User_Location','Bio','createdDateTime','verificationStatus','favouritesCount','followersCount','friendsCount'])
        return tweets_df

    def save_results_as_csv(self,dataframe):
    # # #     # Converting dataframe to CSV 
        new_format_time_2 = "%Y%m%d_%H%M%S"
        script_time = datetime.datetime.now().strftime(new_format_time_2)
        csv_name= f"C:/Users/USER/Desktop/tweets_downloaded_{str(script_time)}.csv"
        dataframe.to_csv(path_or_buf=csv_name,header=True,index=False)


if __name__ == "__main__":
    tweets = Twitter_etl()
    tweets_dataframe = tweets.scrape_tweets(text_query='Endsars',count=1000)
    tweets_csv=tweets.save_results_as_csv(dataframe=tweets_dataframe)
    print(tweets_dataframe)


        




