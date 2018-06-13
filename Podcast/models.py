from django.db import models
from tinymce import HTMLField
from django.template.defaultfilters import slugify
from django.utils import timezone

class Podcast(models.Model):
    Name = models.CharField(max_length = 140,blank=False,null=True)
    Author = models.CharField(max_length = 20,blank=False,null=True)
    Description = HTMLField('',blank=False,null=True) # Tinymce richtext editor
    Background_Image = models.FileField(upload_to = 'thumbnails/',blank=False,null=True)
    Episode_Count = models.IntegerField(null=True,blank=False)
    Created_Date = models.DateTimeField(editable=False)
    Total_Listen_Time = models.BigIntegerField(null=True,blank=False)
    slug = models.SlugField(default='no-slug', max_length=100, blank=True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.Name)
            self.Created_Date = timezone.now()
        super(Podcast, self).save(*args, **kwargs)