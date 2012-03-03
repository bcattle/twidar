from django.db import models

# Philosophically, define few constraints, so no required=True, no unique=True

class ExtraMixin(models.Model):
    """
    A mixin that attempts to assign values to named fields
    in the model. If a field isn't found, the extra is saved
    """
    extra = models.TextField(max_length=2000, null=True)

    def __init__(self, obj=None, *args, **kwargs):
        super(Status, self).__init__(*args, **kwargs)
        if obj:
            # Iterate through fields in status,
            # if they exist in model set them appropriately,
            # otherwise save to 'extras' string
            pass

    class Meta:
        abstract = True


class TwitterUserProfile(ExtraMixin):
    background_color = models.CharField(max_length=6)
    background_image_url = models.URLField()
    background_image_url_https = models.URLField()
    background_tile = models.BooleanField()
    image_url = models.URLField()
    image_url_https = models.URLField()
    link_color = models.CharField(max_length=6)
    sidebar_border_color = models.CharField(max_length=6)
    sidebar_fill_color = models.CharField(max_length=6)
    text_color = models.CharField(max_length=6)
    use_background_image = models.BooleanField()


class TwitterUser(ExtraMixin):
    contributors_enabled = models.BooleanField(null=True)
    created_at = models.DateTimeField(null=True)
    default_profile = models.BooleanField(null=True)
    default_profile_image = models.BooleanField(null=True)
    description = models.CharField(max_length=1000)
    favourites_count = models.PositiveIntegerField()
    follow_request_sent = models.BooleanField(null=True)
    followers_count = models.PositiveIntegerField()
    following = models.BooleanField(null=True)
    friends_count = models.PositiveIntegerField()
    geo_enabled = models.BooleanField(null=True)
    id_str = models.CharField(max_length=50)
    is_translator = models.BooleanField(null=True)
    lang = models.CharField(max_length=10)
    listed_count = models.PositiveIntegerField()
    location = models.CharField(max_length=250)
    name = models.CharField(max_length=50)
    #notifications
    profile = models.OneToOneField(TwitterUserProfile)
    protected = models.BooleanField(null=True)
    screen_name = models.CharField(max_length=50)
    show_all_inline_media = models.BooleanField(null=True)
    statuses_count = models.PositiveIntegerField()
    time_zone = models.CharField(max_length=50)
    url = models.URLField()
    utc_offset = models.IntegerField()
    verified = models.BooleanField(null=True)


class TweetEntity(ExtraMixin):
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

    def fill_sizes(self, obj):


class UserMentionEntity(TweetEntity):
    id_str = models.CharField(max_length=50, null=True)
    screen_name = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    #user = models.ForeignKey(TwitterUser)

# TODO: define a TwitterIdField


class Status(ExtraMixin):
    """
    Model that holds a single tweet
    """
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

    def fill_entities(self, status):
        """
        Save the entities field
        """
        hashtags = status.entities.get('hashtags', [])
        if hashtags:
            self.entities_hashtags = HashtagEntity(hashtags)
        urls = status.entities.get('urls', [])
        if urls:
            self.entities_urls = UrlEntity(urls)
        user_mentions = status.entities.get('user_mentions', [])
        if user_mentions:
            self.entities_user_mentions = UserMentionEntity(user_mentions)
        media = status.entities.get('media', [])
        if media:
            self.entities_media = MediaEntity(media)
