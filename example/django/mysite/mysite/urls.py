# coding=utf-8

##0
# from django.conf.urls import patterns, include, url
# from django.contrib import admin
# 
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
# )

##1
# from django.conf.urls import patterns, url
# 
# from polls import views
# 
# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index'),
# )

##2
# from django.conf.urls import patterns, url #old
from django.conf.urls import patterns, include, url # new

from polls import views

urlpatterns = patterns('',
    # url(r'^polls/', include('polls.urls')), # new old
    url(r'^polls/', include('polls.urls', namespace="polls")), # new
    # url(r'^$', views.index, name='index'),
)







