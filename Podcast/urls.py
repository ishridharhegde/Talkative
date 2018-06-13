from django.conf.urls import url, include
from Podcast.views import *

urlpatterns = [
url(r'^create/$',CreatePodcastView,name="Create Podcast Page"),
url(r'^archives/$',PodcastListView,name="Podcast List Page"),
url(r'^(?P<slug>[-\w]+)/$',PodcastDetailView,name='Podcast Detail Page'), #Podcast Details page
url(r'^(?P<slug>[-\w]+)/edit/$',PodcastEditView,name="Podcast Edit Info"),
url(r'^(?P<slug>[-\w]+)/delete/$',PodcastDeleteView,name="Delete Podcast"),
url(r'^(?P<slug>[-\w]+)/newepisode/$',CreateEpisodeView,name="Create an Episode"),
url(r'^(?P<slug>[-\w])/episode/(?P<epi_slug>[-\w]+)/$',EpisodeDetailView,name="Episode Details"),
]