from django.db import models
from tinymce import HTMLField
from django.template.defaultfilters import slugify

class Podcast(models.Model):
    Name = models.CharField(max_length = 140,blank=False,null=True)
    Author = models.CharField(max_length = 20,blank=False,null=True)
    Description = HTMLField('',blank=False,null=True) # Tinymce richtext editor
    Background_Image = models.FileField(upload_to = 'thumbnails/',blank=False,null=True)
    Episode_Count = models.IntegerField(null=True,blank=False)
    Created_Date = models.IntegerField(null=True,blank=False)
    Total_Listen_Time = models.BigIntegerField(null=True,blank=False)
    Slug = models.SlugField(default='no-slug', max_length=100, blank=True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        if not self.id:
            self.Slug = slugify(self.Name)
        super(Podcast, self).save(*args, **kwargs)