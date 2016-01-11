from django.conf.urls import patterns, url

from website import views

urlpatterns = [
    url(r'(zz)', views.newhomepage, name='newhomepage'),
    url(r'^$', views.oldhomepage, name='oldhomepage'),
]