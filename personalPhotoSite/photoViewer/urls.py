from django.conf.urls import patterns, include, url
from photoViewer import views

# map url to view using a URLconf
urlpatterns = patterns('',
    # url(r'^$', views.PhotoIndexView.as_view(), name='photo_index'),
    url(r'^about/', views.PhotoViewerAboutTemplateView.as_view()),

    url(r'^photos/(?P<filter_type>(date_desc|title_desc|))$', views.PhotoIndexView.as_view(), name='photo_index'),
    url(r'^photos/(?P<pk>\d+)/$', views.PhotoDetailView.as_view(), name='photo_detail'),

    url(r'^albums/$', views.AlbumsIndexView.as_view(), name='albums_index'),
    url(r'^albums/(?P<pk>\d+)/$', views.AlbumDetailView.as_view(), name='album_detail'),

    url(r'^places/$', views. PlacesTemplateView.as_view(), name='places'),


)
