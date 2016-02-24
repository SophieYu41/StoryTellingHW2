#This file retrieves data stream from twitter API and filter the data by keywords
# we are interested in.

from analyze_tweet import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2843768163-8lapJ7O50xPWxkmAwWIhi8kgaOrflPgmG1xQC9W"
access_token_secret = "gaNrKB1BUN1fSX10U7NAtPKv65WwHfbrH8dlQ5j4LxVxf"
consumer_key = "NUCwbIkKkd20W8iHIYoOxlv0b"
consumer_secret = "6P2uOCOb0Xb8ZLkQ17PRTRl05T0BFC9EaToDB5sLSnI1TQONGU"

#This is a basic listener that prints received tweets to add_tweet function
class StdOutListener(StreamListener):

    def on_data(self, data):
        add_tweet(data)
        return True


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords that we are interested in
    stream.filter(track=['hillaryclinton', 'donaldtrump'])