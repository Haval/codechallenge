from django.conf.urls import patterns, url

from apps.challenge import views


urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/join$', views.JoinView.as_view(), name='join'),
	url(r'^create/$', views.CreateView.as_view(), name='create'),
)