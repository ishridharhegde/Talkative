from django.conf.urls import url, include
from Podcast.views import *

urlpatterns = [
url(r'^create/$',CreatePodcastView,name="Create Podcast Page"),
url(r'^archives/$',PodcastListView,name="Podcast List Page"),
url(r'^archives/(?P<slug>[-\w]+)/$',PodcastDetailView,name='Podcast Detail Page'), #Podcast Details page
url(r'^archives/(?P<slug>[-\w]+)/edit/$',PodcastEditView,name="Podcast Edit Info"),
url(r'^archives/(?P<slug>[-\w]+)/delete/$',PodcastDeleteView,name="Delete Podcast"),
url(r'^archives/(?P<slug>[-\w]+)/newepisode/$',CreateEpisodeView,name="Create an Episode"),
url(r'^archives/episode/(?P<slug>[-\w]+)/$',EpisodeDetailView,name="Episode Details"),
url(r'^archives/episode/(?P<slug>[-\w]+)/edit/$',EpisodeEditView,name="Episode Details"),
url(r'^archives/episode/(?P<slug>[-\w]+)/delete/$',EpisodeDeleteView,name="Episode Details"),
]