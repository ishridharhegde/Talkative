from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Podcast.forms import CreatePodcastForm,CreateEpisodeForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from Podcast.models import Podcast,Episode,timezone
from django.views.generic import DetailView

@login_required
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

@login_required
def PodcastEditView(request,slug):
	if request.method == 'POST':
		Podcast_Data = Podcast.objects.get(slug=slug)
		Podcast_Edit_Form = CreatePodcastForm(request.POST, request.FILES,instance=Podcast_Data)
		if Podcast_Edit_Form.is_valid():
			Podcast_Edit_Form.save()
			url = '/podcast/archive/' + str(slug)
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

@login_required
def PodcastDeleteView(request,slug):
	Podcast_Obj = Podcast.objects.get(slug=slug)
	Podcast_Obj.delete()
	return HttpResponseRedirect('/podcast/archives')


@login_required
def CreateEpisodeView(request,slug):
	if request.method == 'POST':
		form = CreateEpisodeForm(request.POST, request.FILES)
		if form.is_valid():
			Form_Instance_Copy = form.save(commit=False)
			Form_Instance_Copy.Created_By_User = str(request.user.username)
			Form_Instance_Copy.Pod_Slug = slug
			Form_Instance_Copy.save()
			form.save()
			return HttpResponseRedirect('/podcast/archive/'+ slug)
		else:
			return render(request, 'Podcast/CreateEpisode.html', {'CreateEpisode': CreateEpisodeForm})
	return render(request, 'Podcast/CreateEpisode.html', {'CreateEpisodeForm': CreateEpisodeForm})

def EpisodeDetailView(request,slug):
	Episode_Data = Episode.objects.get(slug=slug)
	return render(request, 'Podcast/EpisodeDetail.html', {'Episode_Data':Episode_Data})

@login_required
def EpisodeEditView(request,slug):
	if request.method == 'POST':
		Episode_Data = Episode.objects.get(slug=slug)
		Episode_Edit_Form = CreateEpisodeForm(request.POST, request.FILES,instance=Episode_Data)
		if Episode_Edit_Form.is_valid():
			Form_Instance_Copy = Episode_Edit_Form.save(commit=False)
			Form_Instance_Copy.Last_Updated_At = timezone.now()
			Form_Instance_Copy.save()
			Form_Instance_Copy.save()
			Episode_Edit_Form.save()
			url = '/podcast/archive/episode/' + str(slug)
			print(url)
			return HttpResponseRedirect(url)
		else:
			Episode_Edit_Form = CreatePodcastForm(instance=request.user,initial={'Name':Episode_Data.Name,'Episode_Descriptionn':Episode_Data.Episode_Description,'Episode_File':Episode_Data.Episode_File,'Episode_Thumbnail':Episode_Data.Episode_Thumbnail})
			args = {'Episode_Edit_Form':Episode_Edit_Form}
			return render(request,'Podcast/EpisodeDetailEdit.html',args)
	else:	
		Episode_Data = Episode.objects.get(slug=slug)
		Episode_Edit_Form = CreateEpisodeForm(instance=request.user,initial={'Name':Episode_Data.Name,'Episode_Description':Episode_Data.Episode_Description,'Episode_File':Episode_Data.Episode_File,'Episode_Thumbnail':Episode_Data.Episode_Thumbnail})
		args = {'Episode_Edit_Form':Episode_Edit_Form}
		return render(request,'Podcast/EpisodeDetailEdit.html',args)

@login_required	
def EpisodeDeleteView(request,slug):
	Episode_Obj = Episode.objects.get(slug=slug)
	Podcast_Link = Episode_Obj.Pod_Slug
	Episode_Obj.delete()
	return HttpResponseRedirect('/podcast/archives/'+str(Podcast_Link))