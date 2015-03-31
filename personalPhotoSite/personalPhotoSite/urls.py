from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.conf import settings
#Root URLconfs

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personalPhotoSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url (r'^<app_name>/', include ('<app_name>.urls')),

    url(r'^photoViewer/', include('photoViewer.urls', namespace='photoViewer')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
