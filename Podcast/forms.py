from django import forms
from Podcast.models import Podcast,Episode
from tinymce import TinyMCE

class CreatePodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ('Name','Author','Description','Background_Image',)

class CreateEpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ('Name','Episode_Description','Episode_File','Episode_Thumbnail')