from django import forms
from Podcast.models import Podcast
from tinymce import TinyMCE

class CreatePodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ('Name','Author','Description','Background_Image',)