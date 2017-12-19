from django.conf.urls import url

from .views import upload, search

urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^upload/$', upload, name='upload_file'),
]
