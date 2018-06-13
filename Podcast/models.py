from django.db import models
from tinymce import HTMLField
from django.template.defaultfilters import slugify
from django.utils import timezone

class Podcast(models.Model):
    Name = models.CharField(max_length = 140,blank=False,null=True)
    Author = models.CharField(max_length = 20,blank=False,null=True)
    Description = models.TextField(max_length=500,blank=False,null=True)
    Background_Image = models.FileField(upload_to = 'Podcast_Thumbnails/',blank=False,null=True)
    Episode_Count = models.IntegerField(null=True,blank=False)
    Created_Date = models.DateTimeField(editable=False,blank=False,null=True)
    Total_Listen_Time = models.BigIntegerField(null=True,blank=False)
    Created_By_User = models.CharField(max_length = 140,blank=False,null=True)
    slug = models.SlugField(default='no-slug', max_length=100, blank=True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.Name)
            self.Created_Date = timezone.now()
        super(Podcast, self).save(*args, **kwargs)

class Episode(models.Model):
    Name = models.CharField(max_length = 300,blank=False,null=True)
    Date_Of_Publication = models.DateTimeField(editable=False,blank=False,null=True)
    Last_Updated_At = models.DateTimeField(blank=False,null=True)
    Episode_Description = HTMLField('',blank=False,null=True) # Show Notes
    Episode_File = models.FileField(upload_to = 'Episode_File/',blank=False,null=True)
    Episode_Thumbnail = models.FileField(upload_to = 'Episode_Thumbnails/',blank=False,null=True)
    Created_By_User = models.CharField(max_length = 140,blank=False,null=True)
    Number_of_Views = models.BigIntegerField(null=True,blank=False)
    Number_Of_Likes = models.IntegerField(null=True,blank=False)
    Pod_Slug =  models.SlugField(default='no-slug', max_length=300, blank=True)
    epi_slug = models.SlugField(max_length=300, unique=True, null=True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        if not self.id:
            self.epi_slug = '/'.join((self.Pod_Slug,slugify(self.Name)))
            self.Date_Of_Publication = timezone.now()
            self.Last_Updated_At = timezone.now()
        super(Episode, self).save(*args, **kwargs)