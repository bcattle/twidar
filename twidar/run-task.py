# Setup django environment
# From http://www.b-list.org/weblog/2007/sep/22/standalone-django-scripts/
from django.core.management import setup_environ
import settings
setup_environ(settings)

from monitor.tasks import tweet_stream_task
tweet_stream_task(track_list=['taskrabbit'])