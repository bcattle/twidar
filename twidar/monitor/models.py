import simplejson as json
from django.db import models

# Philosophically, define few constraints, so no required=True, no unique=True

class ExtraMixin(models.Model):
    """
    A mixin that attempts to assign values to named fields
    in the model. If a field isn't found, the extra is saved
    """
    extra = models.TextField(max_length=2000, null=True)

    def __init__(self, *args, **kwargs):
        obj_in = kwargs.pop('obj', None)
        super(ExtraMixin, self).__init__(*args, **kwargs)
        if obj_in:
            # TODO: cache this
            field_names = [field.name for field in self._meta.fields]
            # Iterate through incoming fields,
            # look for a fill_xxx method
            # look for a field in the model to set
            #  --> otherwise save to 'extras' string
            extra_objs = {}
            # Input is either a class, or a dict
            if hasattr(obj_in, '__dict__'):
                items_dict = obj_in.__dict__
            else:
                items_dict = obj_in

            for k,v in items_dict.items():
                # Skip the id field
                if k == 'id':
                    continue
                fill_method = getattr(self, 'fill_%s' % k, None)
                if fill_method:
                    fill_method(v)
                elif k in field_names:
                    setattr(self, k, v)
                else:
                    # No match, add to extras if not in include list
                    if k not in getattr(self, 'ignore_fields', []):
                        extra_objs[k] = v
            # Serialize extra_objs
            if extra_objs:
                self.extra = json.dumps(extra_objs)

    class Meta:
        abstract = True


class TwitterUserProfile(ExtraMixin):
    background_color = models.CharField(max_length=6, null=True)
    background_image_url = models.URLField(null=True)
    background_image_url_https = models.URLField(null=True)
    background_tile = models.NullBooleanField(null=True)
    image_url = models.URLField(null=True)
    image_url_https = models.URLField(null=True)
    link_color = models.CharField(max_length=6, null=True)
    sidebar_border_color = models.CharField(max_length=6, null=True)
    sidebar_fill_color = models.CharField(max_length=6, null=True)
    text_color = models.CharField(max_length=6, null=True)
    use_background_image = models.NullBooleanField(null=True)


class TwitterUser(ExtraMixin):
    contributors_enabled = models.NullBooleanField(null=True)
    created_at = models.DateTimeField(null=True)
    default_profile = models.NullBooleanField(null=True)
    default_profile_image = models.NullBooleanField(null=True)
    description = models.CharField(max_length=1000, null=True)
    favourites_count = models.PositiveIntegerField(null=True)
    follow_request_sent = models.NullBooleanField(null=True)
    followers_count = models.PositiveIntegerField(null=True)
    following = models.NullBooleanField(null=True)
    friends_count = models.PositiveIntegerField(null=True)
    geo_enabled = models.NullBooleanField(null=True)
    id_str = models.CharField(max_length=50, null=True)
    is_translator = models.NullBooleanField(null=True)
    lang = models.CharField(max_length=10, null=True)
    listed_count = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=50, null=True)
    #notifications
    #profile = models.OneToOneField(TwitterUserProfile)
    protected = models.NullBooleanField(null=True)
    screen_name = models.CharField(max_length=50, null=True)
    show_all_inline_media = models.NullBooleanField(null=True)
    statuses_count = models.PositiveIntegerField(null=True)
    time_zone = models.CharField(max_length=50, null=True)
    url = models.URLField(null=True)
    utc_offset = models.IntegerField(null=True)
    verified = models.NullBooleanField(null=True)

    profile_background_color = models.CharField(max_length=6, null=True)
    profile_background_image_url = models.URLField(null=True)
    profile_background_image_url_https = models.URLField(null=True)
    profile_background_tile = models.NullBooleanField(null=True)
    profile_image_url = models.URLField(null=True)
    profile_image_url_https = models.URLField(null=True)
    profile_link_color = models.CharField(max_length=6, null=True)
    profile_sidebar_border_color = models.CharField(max_length=6, null=True)
    profile_sidebar_fill_color = models.CharField(max_length=6, null=True)
    profile_text_color = models.CharField(max_length=6, null=True)
    profile_use_background_image = models.NullBooleanField(null=True)

#    def __init__(self, *args, **kwargs):
#        super(TwitterUser, self).__init__(*args, **kwargs)
#        self.profile = TwitterUserProfile()


# TODO: define a TwitterIdField


class Status(ExtraMixin):
    """
    Model that holds a single tweet
    """
    # TODO: sort out the commented fields
    author = models.ForeignKey(TwitterUser, related_name='statuses', null=True)
    contributors = models.CharField(max_length=250, null=True)     # Stores a list of user ids
    #coordinates
    created_at = models.DateTimeField(null=True)
    #entities_hashtags = models.ManyToManyField(HashtagEntity, related_name='statuses', null=True)
    #entities_media = models.ManyToManyField(MediaEntity, related_name='statuses', null=True)
    #entities_urls = models.ManyToManyField(UrlEntity, related_name='statuses', null=True)
    #entities_user_mentions = models.ManyToManyField(UserMentionEntity, related_name='statuses', null=True)
    favorited = models.NullBooleanField(null=True)
    geo = models.CharField(max_length=250, null=True)      # Stores GeoJSON, e.g.
                                                            # { "type":"Point", "coordinates":[37.78029, -122.39697] }
    id_str = models.CharField(max_length=50, null=True)
    in_reply_to_screen_name = models.CharField(max_length=50, null=True)
    in_reply_to_status_id_str = models.CharField(max_length=50, null=True)
    in_reply_to_user_id_str = models.CharField(max_length=50, null=True)
    retweeted_status = models.ForeignKey('Status', null=True)       # Ooh, recursive foreign key
    #place
    possibly_sensitive = models.NullBooleanField(null=True)
    possibly_sensitive_editable = models.NullBooleanField(null=True)
    retweet_count = models.PositiveIntegerField(null=True)
    retweeted = models.NullBooleanField(null=True)
    source = models.CharField(max_length=250, null=True)
    source_url = models.URLField(null=True)
    text = models.CharField(max_length=150, null=True)
    truncated = models.NullBooleanField(null=True)
    user = models.ForeignKey(TwitterUser, related_name='statuses_user', null=True)

    ignore_fields = ('in_reply_to_status_id', 'in_reply_to_user_id')

    def __unicode__(self):
        return 'Status: %s' % self.text[:75]

    def fill_entities(self, entities):
        """
        Save the entities field
        """
        self.save()         # Need this to give FKs an id
        hashtags = entities.get('hashtags', [])
        if hashtags:
            for hashtag in hashtags:
                h = HashtagEntity(obj=hashtag, status=self)
                h.save()
        urls = entities.get('urls', [])
        if urls:
            for url in urls:
                u = UrlEntity(obj=url, status=self)
                u.save()
        user_mentions = entities.get('user_mentions', [])
        if user_mentions:
            for mention in user_mentions:
                ent = UserMentionEntity(obj=mention, status=self)
                ent.save()
        medias = entities.get('media', [])
        if medias:
            for media in medias:
                m = MediaEntity(obj=media, status=self)
                m.save()

    def fill_author(self, author):
        if self.user:
            if author.id_str == self.user.id_str:
                self.author = self.user
                return

        new_user = TwitterUser(obj=author)
        new_user.save()
        self.author = new_user

    def fill_user(self, user):
        if self.author:
            if user.id_str == self.author.id_str:
                self.user = self.author
                return

        new_user = TwitterUser(obj=user)
        new_user.save()
        self.user = new_user

    def fill_retweeted_status(self, status):
        self.retweeted_status = Status(obj=status)      # Need to save this?


class TweetEntity(ExtraMixin):
    status = models.ForeignKey(Status, related_name='%(class)s')
    indices = models.CharField(max_length=50, null=True)       # list = str

    class Meta:
        abstract = True


class HashtagEntity(TweetEntity):
    text = models.CharField(max_length=50, null=True)


class UrlEntity(TweetEntity):
    url = models.URLField(null=True)
    display_url = models.CharField(max_length=255, null=True)
    expanded_url = models.URLField(null=True)


class MediaEntity(UrlEntity):
    media_url = models.URLField(null=True)
    media_url_https = models.URLField(null=True)
    id_str = models.CharField(max_length=50, null=True)
    sizes = models.CharField(max_length=255, null=True)        # dict = str
    type = models.CharField(max_length=50, null=True)

    def fill_sizes(self, sizes):
        """ Process the ``sizes`` field into a string """
        self.sizes = json.dumps(sizes)


class UserMentionEntity(TweetEntity):
    id_str = models.CharField(max_length=50, null=True)
    screen_name = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    #user = models.ForeignKey(TwitterUser)
