#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "127884553-TqitaQ5yWajIsxoJRXB0zMFCvqsLkVsIUtX0j4EA"
access_token_secret = "JQkefONCrcDDFezZvICbX3Sw8FUYpyQs9bqoIVIEzi1Du"
consumer_key = "QnDUp41BaQPi9buXTMmJVQ7Vg"
consumer_secret = "2eYxYHmbrxUIbbZNF0sBtlOARlwmG04DfisJEpJeNgmTGLPH0z"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
