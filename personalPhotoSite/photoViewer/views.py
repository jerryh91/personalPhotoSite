from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from photoViewer.models import Photo, Album

# Create your views here.
# Each View: serves a specific function and has a specific template


#By default:
#Uses <app name>/<model name>_detail.html template
#Unless specified by template_name


#Base View > TemplateView:
#Renders a given template, with the context containing parameters captured in the URL.

class PhotoViewerAboutView (generic.TemplateView):
    template_name = 'photoViewer/photoViewer_about.html'

#Generic Display View > ListView:
#
class PhotoIndexView (generic.ListView):
    template_name = 'photoViewer/photo_index.html'
    context_object_name = 'latest_photo_list'

    def get_queryset(self):
        return Photo.objects.order_by('-date_taken')[:5]

class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'photoViewer/photo_detail.html'

class AlbumsIndexView(generic.ListView):
    template_name = 'photoViewer/albums_index.html'
    context_object_name = 'latest_albums_list'

    def get_queryset(self):
        return Album.objects.order_by('-date_created')[:5]


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'photoViewer/albums_detail.html'