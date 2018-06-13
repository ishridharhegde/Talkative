from django.shortcuts import render
from Podcast.forms import CreatePodcastForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from Podcast.models import Podcast
from django.views.generic import DetailView

def CreatePodcastView(request):
	if request.method == 'POST':
		form = CreatePodcastForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/podcast/archives/')
		else:
			return render(request, 'Podcast/CreatePodcast.html', {'CreatePodcastForm': CreatePodcastForm})
	return render(request, 'Podcast/CreatePodcast.html', {'CreatePodcastForm': CreatePodcastForm})

def PodcastListView(request):
	PodcastList = Podcast.objects.all().order_by("-Created_Date")
	return render(request, 'Podcast/PodcastList.html', {'PodcastList': PodcastList})

def PodcastDetailView(request,slug):
	Podcast_Data = Podcast.objects.get(slug=slug)
	return render(request, 'Podcast/PodcastDetail.html', {'Podcast_Data':Podcast_Data })

def PodcastEditView(request,slug):
	if request.method == 'POST':
		Podcast_Data = Podcast.objects.get(slug=slug)
		Podcast_Edit_Form = CreatePodcastForm(request.POST, request.FILES,instance=Podcast_Data)
		if Podcast_Edit_Form.is_valid():
			Podcast_Edit_Form.save()
			url = '/podcast/' + str(slug)
			return HttpResponseRedirect(url)
		else:
			Podcast_Edit_Form = CreatePodcastForm(instance=request.user,initial={'Name':Podcast_Data.Name,'Author':Podcast_Data.Author,'Description':Podcast_Data.Description,'Background_Image':Podcast_Data.Background_Image})
			args = {'Podcast_Edit_Form':Podcast_Edit_Form}
			return render(request,'Podcast/PodcastDetailEdit.html',args)
	else:	
		Podcast_Data = Podcast.objects.get(slug=slug)
		Podcast_Edit_Form = CreatePodcastForm(instance=request.user,initial={'Name':Podcast_Data.Name,'Author':Podcast_Data.Author,'Description':Podcast_Data.Description,'Background_Image':Podcast_Data.Background_Image})
		args = {'Podcast_Edit_Form':Podcast_Edit_Form}
		return render(request,'Podcast/PodcastDetailEdit.html',args)

def PodcastDeleteView(request,slug):
	Podcast_Obj = Podcast.objects.get(slug=slug)
	Podcast_Obj.delete()
	return HttpResponseRedirect('/podcast/archives')