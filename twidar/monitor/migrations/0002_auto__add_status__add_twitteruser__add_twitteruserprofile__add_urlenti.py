# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Status'
        db.create_table('monitor_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statuses', null=True, to=orm['monitor.TwitterUser'])),
            ('contributors', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('favorited', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('geo', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('id_str', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('in_reply_to_screen_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('in_reply_to_status_id_str', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('in_reply_to_user_id_str', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('possibly_sensitive', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('possibly_sensitive_editable', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('retweet_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('retweeted', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('source_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('truncated', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statuses_user', null=True, to=orm['monitor.TwitterUser'])),
        ))
        db.send_create_signal('monitor', ['Status'])

        # Adding model 'TwitterUser'
        db.create_table('monitor_twitteruser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True)),
            ('contributors_enabled', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('default_profile', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('default_profile_image', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('favourites_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('follow_request_sent', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('followers_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('following', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('friends_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('geo_enabled', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('id_str', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('is_translator', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('listed_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('protected', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('show_all_inline_media', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('statuses_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('time_zone', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('utc_offset', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('verified', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('profile_background_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('profile_background_image_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('profile_background_image_url_https', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('profile_background_tile', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('profile_image_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('profile_image_url_https', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('profile_link_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('profile_sidebar_border_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('profile_sidebar_fill_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('profile_text_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('profile_use_background_image', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('monitor', ['TwitterUser'])

        # Adding model 'TwitterUserProfile'
        db.create_table('monitor_twitteruserprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True)),
            ('background_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('background_image_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('background_image_url_https', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('background_tile', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image_url_https', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('link_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('sidebar_border_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('sidebar_fill_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('text_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('use_background_image', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('monitor', ['TwitterUserProfile'])

        # Adding model 'UrlEntity'
        db.create_table('monitor_urlentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='urlentity', to=orm['monitor.Status'])),
            ('indices', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('display_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('expanded_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('monitor', ['UrlEntity'])

        # Adding model 'MediaEntity'
        db.create_table('monitor_mediaentity', (
            ('urlentity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['monitor.UrlEntity'], unique=True, primary_key=True)),
            ('media_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('media_url_https', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('id_str', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('sizes', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('monitor', ['MediaEntity'])

        # Adding model 'HashtagEntity'
        db.create_table('monitor_hashtagentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='hashtagentity', to=orm['monitor.Status'])),
            ('indices', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('monitor', ['HashtagEntity'])

        # Adding model 'UserMentionEntity'
        db.create_table('monitor_usermentionentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('extra', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='usermentionentity', to=orm['monitor.Status'])),
            ('indices', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('id_str', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('monitor', ['UserMentionEntity'])


    def backwards(self, orm):
        
        # Deleting model 'Status'
        db.delete_table('monitor_status')

        # Deleting model 'TwitterUser'
        db.delete_table('monitor_twitteruser')

        # Deleting model 'TwitterUserProfile'
        db.delete_table('monitor_twitteruserprofile')

        # Deleting model 'UrlEntity'
        db.delete_table('monitor_urlentity')

        # Deleting model 'MediaEntity'
        db.delete_table('monitor_mediaentity')

        # Deleting model 'HashtagEntity'
        db.delete_table('monitor_hashtagentity')

        # Deleting model 'UserMentionEntity'
        db.delete_table('monitor_usermentionentity')


    models = {
        'monitor.hashtagentity': {
            'Meta': {'object_name': 'HashtagEntity'},
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indices': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hashtagentity'", 'to': "orm['monitor.Status']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'monitor.mediaentity': {
            'Meta': {'object_name': 'MediaEntity', '_ormbases': ['monitor.UrlEntity']},
            'id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'media_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'media_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'sizes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'urlentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['monitor.UrlEntity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'monitor.status': {
            'Meta': {'object_name': 'Status'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'null': 'True', 'to': "orm['monitor.TwitterUser']"}),
            'contributors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'favorited': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'geo': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'in_reply_to_screen_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'in_reply_to_status_id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'in_reply_to_user_id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'possibly_sensitive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'possibly_sensitive_editable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'retweet_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'retweeted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'truncated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses_user'", 'null': 'True', 'to': "orm['monitor.TwitterUser']"})
        },
        'monitor.twitteruser': {
            'Meta': {'object_name': 'TwitterUser'},
            'contributors_enabled': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'default_profile': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'default_profile_image': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'favourites_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'follow_request_sent': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'followers_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'following': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'friends_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'geo_enabled': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'is_translator': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'listed_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'profile_background_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'profile_background_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'profile_background_image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'profile_background_tile': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'profile_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'profile_image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'profile_link_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'profile_sidebar_border_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'profile_sidebar_fill_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'profile_text_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'profile_use_background_image': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'protected': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'show_all_inline_media': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'statuses_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'utc_offset': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'verified': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'monitor.twitteruserprofile': {
            'Meta': {'object_name': 'TwitterUserProfile'},
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'background_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'background_image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'background_tile': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'image_url_https': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'link_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'sidebar_border_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'sidebar_fill_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'text_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'use_background_image': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'monitor.urlentity': {
            'Meta': {'object_name': 'UrlEntity'},
            'display_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'expanded_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indices': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'urlentity'", 'to': "orm['monitor.Status']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'monitor.usermentionentity': {
            'Meta': {'object_name': 'UserMentionEntity'},
            'extra': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_str': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'indices': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usermentionentity'", 'to': "orm['monitor.Status']"})
        }
    }

    complete_apps = ['monitor']
