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

class PhotoViewerAboutTemplateView (generic.TemplateView):
    template_name = 'photoViewer/photoViewer_about.html'

class PlacesTemplateView (generic.TemplateView):
    template_name = "photoViewer/places.html"

#Generic Display View > ListView:
class PhotoIndexView (generic.ListView):
    template_name = 'photoViewer/photo_index.html'
    context_object_name = 'latest_photo_list'

    def get_queryset(self):
        filter_type = self.kwargs['filter_type']
        if filter_type == 'date_desc':
            return Photo.objects.order_by('-date_taken')[:]
        elif filter_type =='title_desc':
            return Photo.objects.order_by('-photo_title')[:]
        else:
            # default ordering
            return Photo.objects.all()[:5]

class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'photoViewer/photo_detail.html'

class AlbumsIndexView(generic.ListView):

    template_name = 'photoViewer/albums_index.html'
    context_object_name = 'latest_albums_list'

    def get_queryset(self):
        #Retrieve filter/order_by type

        return Album.objects.order_by('-date_created')[:5]

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'photoViewer/albums_detail.html'