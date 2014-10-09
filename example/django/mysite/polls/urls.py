##1
# from django.conf.urls import patterns, include, url
# from django.contrib import admin
# 
# urlpatterns = patterns('',
#     url(r'^polls/', include('polls.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# )

##2
# from django.conf.urls import patterns, url
# 
# from polls import views
# 
# urlpatterns = patterns('',
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
#     
#     # the 'name' value as called by the {% url %} template tag
#     url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
#     
#     # added the word 'specifics'
#     url(r'^specifics/(?P<question_id>\d+)/$', views.detail, name='detail'),
#     
# )


##3 --> views.py ##6
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
