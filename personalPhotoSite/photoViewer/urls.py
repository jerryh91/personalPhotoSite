from django.conf.urls import patterns, include, url
from photoViewer import views

# map url to view using a URLconf
urlpatterns = patterns('',
    # url(r'^$', views.PhotoIndexView.as_view(), name='photo_index'),
    url(r'^about/', views.PhotoViewerAboutView.as_view()),
    url(r'^photos/$', views.PhotoIndexView.as_view(), name='photo_index'),
    url(r'^photos/(?P<pk>\d+)/$', views.PhotoDetailView.as_view(), name='photo_detail'),

    url(r'^albums/$', views.AlbumsIndexView.as_view(), name='albums_index'),
    url(r'^albums/(?P<pk>\d+)/$', views.AlbumDetailView.as_view(), name='album_detail'),


)
