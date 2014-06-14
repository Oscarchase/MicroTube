from django.conf.urls import patterns, include, url
from django.contrib import admin

from MicroTube import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='index'),
    url(r'^search', views.SearchView, name='search'),
    url(r'^admin/', include(admin.site.urls)),
)
