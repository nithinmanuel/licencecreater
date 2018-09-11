from django.conf import settings
from django.conf.urls import url
from . import views
urlpatterns = [


# the urls for uploading the document and returning the converted document

    url(r'^document/create/$', views.upload_document, name='upload_document'),

    url(r'^document/(?P<document_id>\d+)/convert/$', views.download_converted_document,
        name='download_converted_document'),


# the urls for performing the CRUD operations 
    url(r'^keyword/create/$', views.create_keyword, name='create_keyword'),


    url(r'^keyword/get/$', views.get_keywords, name='get_keywords'),


    url(r'^keyword/(?P<keyword_id>\d+)/get/$',
        views.single_keyword, name='single_keyword'),


    url(r'^keyword/(?P<keyword_id>\d+)/edit/$',
        views.edit_keyword, name='edit_keyword'),


    url(r'^keyword/(?P<keyword_id>\d+)/delete/$',
        views.delete_keyword, name='delete_keyword'),

    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
    # r'(?P<post>[-\w]+)/$',
    # views.post_detail,
    # name='post_detail'),
]

# if settings.DEBUG:
#urlpatterns += [url(r'^debuginfo/$', views.debug), ]
