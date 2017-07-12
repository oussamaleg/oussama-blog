from django.conf.urls import url, include
from . import views
app_name = 'technology'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<blog_id>[0-9]+)/$', views.blog, name="blog"),
    url(r'^p/(?P<part_id>[0-9]+)/$', views.part, name="part"),
    url(r'^u/(?P<user_id>[0-9]+)/$', views.profile, name="profile")
]
