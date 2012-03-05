from django.contrib import admin
from monitor.models import Status, TwitterUser, HashtagEntity, MediaEntity, UrlEntity, UserMentionEntity

class TwitterUserAdmin(admin.ModelAdmin):
    list_display = ('screen_name', 'name', 'followers_count', 'friends_count', 'statuses_count', 'description', 'id_str',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id_str', 'author', 'text', 'extra')

class HashtagEntityAdmin(admin.ModelAdmin):
    list_display = ('text', 'status', )

class MediaEntityAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'url',)

class UrlEntityAdmin(admin.ModelAdmin):
    list_display = ('url', 'status', )

class UserMentionEntityAdmin(admin.ModelAdmin):
    list_display = ('screen_name', 'status', 'id_str', )

admin.site.register(TwitterUser, TwitterUserAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(HashtagEntity, HashtagEntityAdmin)
admin.site.register(MediaEntity, MediaEntityAdmin)
admin.site.register(UrlEntity, UrlEntityAdmin)
admin.site.register(UserMentionEntity, UserMentionEntityAdmin)