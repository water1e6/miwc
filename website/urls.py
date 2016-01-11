from django.conf.urls import patterns, url

from website import views

urlpatterns = [
    url(r'^$', views.newhomepage, name='newhomepage'),
]