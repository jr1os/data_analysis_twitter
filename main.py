import tweepy

from config import settings
import tweepy as tw
import pandas as pd


consumer_key = settings.consumer_key
consumer_secret = settings.consumer_secret
access_token = settings.access_token
access_token_secret = settings.access_token_secret

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth)

# trends_result = api.get_place_trends(1)
# for trend in trends_result[0]["trends"]:
#    print(trend["name"])


public_tweets = api.home_timeline()

# for tweet in public_tweets:
#    print(tweet._json.keys())

query_search = "#ENEM" + " -filter:retweets"

# woeid = 23424768
cursor_tweets = tw.Cursor(api.search_tweets, q=query_search).items(10)

for tweet in cursor_tweets:
    print(tweet.created_at)
    print(tweet.text)

twkeys = tweet._json.keys()

tweets_dict = {}

query_search = "#ENEM" + " -filter:retweets"
cursor_tweets = tw.Cursor(api.search_tweets, since="2021-09-03", until="2021-09-10", q=query_search).items(20000)

for tweet in cursor_tweets:
    for key in tweets_dict.keys():
        try:
            twvalue = tweet._json[key]
            tweets_dict[key].append(twvalue)
        except KeyError:
            twvalue = ""
            if tweets_dict[key] is None:
                tweets_dict[key] = [twvalue]
            else:
                tweets_dict[key].append(twvalue)
        except:
            tweets_dict[key] = [twvalue]

dfTweets = pd.DataFrame.from_dict(tweets_dict)

dfTweets.head()

dfTweets.to_csv("tweetsENEM2.csv", index=False)