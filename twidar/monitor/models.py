from django.db import models

# Philosophically, define few constaints
# so no required=True, no unique=True

class TwitterUser(models.Model):
    id_str = models.CharField(max_length=50)

class TweetEntity(models.Model):
    indices = models.CharField(max_length=50, null=True)       # list = str
    # Anything else that isn't otherwise covered
    extra = models.TextField(max_length=2000, null=True)

    class Meta:
        abstract = True

class HashtagEntity(TweetEntity):
    text = models.CharField(max_length=50, null=True)

class UrlEntity(TweetEntity):
    url = models.URLField(null=True)
    display_url = models.CharField(max_length=255, null=True)
    expanded_url = models.URLField(null=True)
    # Character positions in the tweet that the media was extracted from

class MediaEntity(UrlEntity):
    media_url = models.URLField(null=True)
    media_url_https = models.URLField(null=True)
    id_str = models.CharField(max_length=50, null=True)
    sizes = models.CharField(max_length=255, null=True)        # dict = str
    type = models.CharField(max_length=50, null=True)

class UserMentionEntity(TweetEntity):
    id_str = models.CharField(max_length=50, null=True)
    screen_name = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    #user = models.ForeignKey(TwitterUser)

# TODO: define a TwitterIdField

class Status(models.Model):
    """
    Model that holds a single tweet
    """
    def __init__(self, status=None, *args, **kwargs):
        super(Status, self).__init__(*args, **kwargs)
        if status:
            # Iterate through fields in status,
            # if they exist in model set them appropriately,
            # otherwise save to 'extras' string
            pass

    # TODO: sort out the commented fields

    author = models.ForeignKey(TwitterUser, related_name='statuses')
    contributors = models.CharField(max_length=250)     # Stores a list of user ids
    #coordinates
    created_at = models.DateTimeField()
    entities_hashtags = models.ManyToManyField(HashtagEntity, null=True)
    entities_media = models.ManyToManyField(MediaEntity, null=True)
    entities_urls = models.ManyToManyField(UrlEntity, null=True)
    entities_user_mentions = models.ManyToManyField(UserMentionEntity, null=True)
    favorited = models.BooleanField()
    geo = models.CharField(max_length=250)      # Stores GeoJSON, e.g.
                                                # { "type":"Point", "coordinates":[37.78029, -122.39697] }
    id_str = models.CharField(max_length=50, unique=True)
    in_reply_to_screen_name = models.CharField(max_length=50)
    in_reply_to_status_id_str = models.CharField(max_length=50)
    in_reply_to_user_id_str = models.CharField(max_length=50)
    #place
    possibly_sensitive = models.BooleanField()
    possibly_sensitive_editable = models.BooleanField()
    retweet_count = models.PositiveIntegerField()
    retweeted = models.BooleanField()
    source = models.CharField(max_length=250)
    source_url = models.URLField()
    text = models.CharField(max_length=150)
    truncated = models.BooleanField()
    user = models.ForeignKey(TwitterUser, related_name='statuses')