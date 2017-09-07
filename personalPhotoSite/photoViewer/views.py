from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from photoViewer.models import Photo, Album
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
from .forms import PhotoUploadForm
from .models import Photo

# Create your views here.
# Each View: serves a specific function and has a specific template


#By default:
#Uses <app name>/<model name>_detail.html template
#Unless specified by template_name


#Base View > TemplateView:
#Renders a given template, with the context containing parameters captured in the URL.
class PhotoUploadView(FormView):
    template_name = 'photoViewer/profile_image_form.html'
    #form_class:
    #in template html:
    #will produce file selection box to choose file to upload 
    form_class = PhotoUploadForm

    def form_valid(self, form):
        #retrieve 'image': field in forms
        #from POST from 'files' dict
        profile_image = Photo(
            photo_img=self.get_form_kwargs().get('files')['photo_img'], 
            photo_title=self.get_form_kwargs().get('data')['photo_title'],
            date_taken=self.get_form_kwargs().get('data')['date_taken'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('photoViewer:profile_image', kwargs={'pk': self.id})

class ProfileDetailView(DetailView):
    model = Photo
    template_name = 'photoViewer/profile_image.html'
    context_object_name = 'image'

class PhotoViewerAboutTemplateView (generic.TemplateView):
    template_name = 'photoViewer/photoViewer_about.html'

class PlacesTemplateView (generic.TemplateView):
    template_name = "photoViewer/places.html"

#Generic Display View > ListView:
class PhotoIndexView (generic.ListView):
    template_name = 'photoViewer/photo_index.html'
    context_object_name = 'latest_photo_list'

    def get_queryset(self):
        #comments
        filter_type = self.kwargs['filter_type']
        if filter_type == 'date_oldtonew':
            return Photo.objects.order_by('date_taken')[:]
        elif filter_type == 'date_newtoold':
            return Photo.objects.order_by('-date_taken')[:]
        elif filter_type =='title_ztoa':
            return Photo.objects.order_by('-photo_title')[:]
        elif filter_type =='title_atoz':
            return Photo.objects.order_by('photo_title')[:]
        else:
            # default ordering
            return Photo.objects.all()[:]

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

