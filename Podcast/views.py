from django.shortcuts import render
from Podcast.forms import CreatePodcastForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from Podcast.models import Podcast

def CreatePodcastView(request):
	if request.method == 'POST':
		form = CreatePodcastForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/podcast/archives/')
		else:
			return render(request, 'Podcast/CreatePodcast.html', {'CreatePodcastForm': CreatePodcastForm})
	return render(request, 'Podcast/CreatePodcast.html', {'CreatePodcastForm': CreatePodcastForm})

def ViewPodcastView(request):
	PodcastList = Podcast.objects.all().order_by("-Created_Date")
	return render(request, 'Podcast/ViewPodcasts.html', {'PodcastList': PodcastList})

