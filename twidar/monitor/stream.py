import tweepy
from twidar.settings import TWITTER_USERNAME, TWITTER_PASSWORD
from monitor.tasks import save_tweet

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
