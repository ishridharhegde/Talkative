from django.contrib import admin
from Podcast.models import Podcast,Episode

class PodcastAdmin(admin.ModelAdmin):
    admin.site.register(Podcast)

class EpisodeAdmin(admin.ModelAdmin):
    admin.site.register(Episode)
