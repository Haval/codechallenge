from django.conf.urls import patterns, url

from apps.challenge import views


urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/join$', views.JoinView.as_view(), name='join'),
	url(r'^(?P<pk>\d+)/leave$', views.LeaveView.as_view(), name='leave'),
	url(r'^(?P<pk>\d+)/update$', views.UpdateView.as_view(), name='update'),
	url(r'^create/$', views.CreateView.as_view(), name='create'),
	url(r'^add_rule_template/(?P<rule_count>\d+)$', views.AddRuleTemplate.as_view(), name='add_rule_template'),
)