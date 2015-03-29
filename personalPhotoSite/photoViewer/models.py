from django.db import models


#manage.py makemigrations <app name>: Store changes to models made in app
#manage.py migrate: 
#sync the changes you made to your models with the schema in the database.

# Create your models here.

#photoViewer/: (index) photostream (list all photos) 
class Photo (models.Model):
    photo_title = models.CharField(max_length=200)
    #how to retrieve from metadata of file?
    date_taken = models.DateField('date taken', default=None, blank=True, null=True)
    photo_img = models.ImageField(upload_to = "images/", default= "")
    def __str__(self):              # __unicode__ on Python 2
        return self.photo_title

class Album (models.Model):
    photos = models.ManyToManyField(Photo)
    date_created = models.DateField('date created', default=None, blank=True, null=True)
    album_title = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.album_title