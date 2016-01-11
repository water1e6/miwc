from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

urlpatterns = [
    # Examples: 
    # url(r'^miwc/', include('miwc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#    url(r'^site/', include('website.urls', namespace="site")),
    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('website.urls', namespace='site')),
]