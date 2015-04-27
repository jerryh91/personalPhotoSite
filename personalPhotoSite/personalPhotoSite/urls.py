from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.conf import settings
from personalPhotoSite import views
#Root URLconfs

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personalPhotoSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url (r'^<app_name>/', include ('<app_name>.urls')),

    url(r'^photoViewer/', include('photoViewer.urls', namespace='photoViewer')),
    url(r'^map/$',  views.MapView.as_view(), name='map'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^formset$', views.DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^form$', views.DefaultFormView.as_view(), name='form_default'),
    url(r'^form_by_field$', views.DefaultFormByFieldView.as_view(), name='form_by_field'),
    url(r'^form_horizontal$', views.FormHorizontalView.as_view(), name='form_horizontal'),
    url(r'^form_inline$', views.FormInlineView.as_view(), name='form_inline'),
    url(r'^form_with_files$', views.FormWithFilesView.as_view(), name='form_with_files'),
    url(r'^pagination$', views.PaginationView.as_view(), name='pagination'),
    url(r'^misc$', views.MiscView.as_view(), name='misc'),



)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
