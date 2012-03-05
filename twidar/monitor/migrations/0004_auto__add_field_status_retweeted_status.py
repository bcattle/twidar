# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Status.retweeted_status'
        db.add_column('monitor_status', 'retweeted_status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Status'], null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Status.retweeted_status'
        db.delete_column('monitor_status', 'retweeted_status_id')


    models = {
        'monitor.hashtagentity': {
            'Meta': {'object_name': 'HashtagEntity'},
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indices': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hashtagentity'", 'to': "orm['monitor.Status']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        'monitor.mediaentity': {
            'Meta': {'object_name': 'MediaEntity', '_ormbases': ['monitor.UrlEntity']},
            'id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'media_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'media_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'urlentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['monitor.UrlEntity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'monitor.status': {
            'Meta': {'object_name': 'Status'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'null': 'True', 'to': "orm['monitor.TwitterUser']"}),
            'contributors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'favorited': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'geo': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'in_reply_to_screen_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'in_reply_to_status_id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'in_reply_to_user_id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'possibly_sensitive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'possibly_sensitive_editable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'retweet_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'retweeted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'retweeted_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['monitor.Status']", 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'truncated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses_user'", 'null': 'True', 'to': "orm['monitor.TwitterUser']"})
        },
        'monitor.twitteruser': {
            'Meta': {'object_name': 'TwitterUser'},
            'contributors_enabled': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'default_profile': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'default_profile_image': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'favourites_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'follow_request_sent': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'followers_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'following': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'friends_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'geo_enabled': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'is_translator': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'listed_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'profile_background_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'profile_background_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'profile_background_image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'profile_background_tile': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'profile_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'profile_image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'profile_link_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'profile_sidebar_border_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'profile_sidebar_fill_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'profile_text_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'profile_use_background_image': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'protected': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'show_all_inline_media': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'statuses_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'utc_offset': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'verified': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'monitor.twitteruserprofile': {
            'Meta': {'object_name': 'TwitterUserProfile'},
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'background_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'background_image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'background_tile': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'link_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'sidebar_border_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'sidebar_fill_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'text_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'use_background_image': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'monitor.urlentity': {
            'Meta': {'object_name': 'UrlEntity'},
            'display_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'expanded_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indices': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'urlentity'", 'to': "orm['monitor.Status']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        'monitor.usermentionentity': {
            'Meta': {'object_name': 'UserMentionEntity'},
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'indices': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usermentionentity'", 'to': "orm['monitor.Status']"})
        }
    }

    complete_apps = ['monitor']
