from django.conf.urls import url, include
from Podcast.views import CreatePodcastView, ViewPodcastView
urlpatterns = [
url(r'^create/$',CreatePodcastView,name="Create Podcast Page"),
url(r'^archives/$',ViewPodcastView,name="View Podcast Page"), 
]