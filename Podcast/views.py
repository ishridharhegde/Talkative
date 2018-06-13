from django.shortcuts import render
from Podcast.forms import CreatePodcastForm,CreateEpisodeForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from Podcast.models import Podcast,Episode
from django.views.generic import DetailView

def CreatePodcastView(request):
	if request.method == 'POST':
		form = CreatePodcastForm(request.POST, request.FILES)
		if form.is_valid():
			Form_Instance_Copy = form.save(commit=False)
			Form_Instance_Copy.Created_By_User = str(request.user.username)
			Form_Instance_Copy.save()
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
	Episodes_List = Episode.objects.all().filter(Pod_Slug=slug)
	return render(request, 'Podcast/PodcastDetail.html', {'Podcast_Data':Podcast_Data,'Episodes_List':Episodes_List })

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

def CreateEpisodeView(request,slug):
	if request.method == 'POST':
		form = CreateEpisodeForm(request.POST, request.FILES)
		if form.is_valid():
			Form_Instance_Copy = form.save(commit=False)
			Form_Instance_Copy.Created_By_User = str(request.user.username)
			Form_Instance_Copy.Pod_Slug = slug
			Form_Instance_Copy.save()
			return HttpResponseRedirect('/podcast/'+ slug)
		else:
			return render(request, 'Podcast/CreateEpisode.html', {'CreateEpisode': CreateEpisodeForm})
	return render(request, 'Podcast/CreateEpisode.html', {'CreateEpisodeForm': CreateEpisodeForm})

def EpisodeDetailView(request,epi_slug):
	print(epi_slug)
	Episode_Data = Episode.object.get(epi_slug=epi_slug)
	return render(request, 'Podcast/EpisodeDetail.html', {'Episode_Data':Episode_Data})