import tweepy
from celery.decorators import task
from twidar.settings import TWITTER_USERNAME, TWITTER_PASSWORD


class StreamWatcherListener(tweepy.StreamListener):
    def on_status(self, status):
        save_tweet(status)

    def on_error(self, status_code):
        # TODO: log the error
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        # TODO: backoff delay?
        print 'Snoozing Zzzzzz'


#@task
def tweet_stream_task(follow_list=None, track_list=None):
    """
    Starts the twitter stream API
    """
    if not (follow_list or track_list):
        raise Exception('You need to call start_twitter_stream with a list of users or keywords.')

    # Login info
    auth_handler = tweepy.BasicAuthHandler(TWITTER_USERNAME, TWITTER_PASSWORD)

    stream = tweepy.Stream(auth_handler, StreamWatcherListener(), timeout=None)
    #stream.filter(follow_list, track_list)
    stream.sample()         # Blocks by default

tweets = []

#@task
def save_tweet(status):
    """
    Pushes a status into the database
    """
    tweets.append(status)
    print 'saved tweet'
    return