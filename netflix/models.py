
from django.db import models
from django.utils import timezone
from django.utils.html import format_html 


# Create your models here.
CHARS_MAX_LENGTH: int = 150
class Category(models.Model):
     """Category model class."""
     name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
     description = models.TextField(blank=True, null=True)
     def __str__(self):
        return self.name 

class Tag(models.Model):
    """Tag model class."""

    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)  
    watch_count = models.IntegerField(default=0)  
    def __str__(self):
        return self.name      


class Movie(models.Model):
     """Movie model class."""
     name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
     description = models.TextField(blank=True, null=True)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     tags = models.ManyToManyField(Tag)
     watch_count = models.IntegerField(default=0)
     file = models.FileField(upload_to='movies/')
     preview_image = models.ImageField(upload_to='preview_images/')
     date_created = models.DateTimeField(default=timezone.now)
     def __str__(self):
        return self.name
     def preview(self, movie):
        """Render preview image as html image."""

        return format_html(
            f'<img style="height: 200px" src="/media/{movie.preview_image}" />'
        )
     def video(self, movie):
        """Render movie video as html image."""

        return format_html(
            '''
            <video width="320" height="240" controls>
                <source src="%s" type="video/mp4">
                Your browser does not support the video tag.
            </video>''' % movie.file
        )

     preview.short_description = 'Movie image'
     video.short_description = 'Movie video'
     list_display = ['name', 'preview', 'video', 'description']
     
   

     

