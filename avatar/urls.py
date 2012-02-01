from django.conf.urls import url

from avatar import views

urlpatterns = [
    url(r'^add/$', views.add, name='avatar_add'),
    url(r'^change/$', views.change, name='avatar_change'),
    url(r'^delete/$', views.delete, name='avatar_delete'),
    url(r'^render_primary/(?P<user>[\w\d\@\.\-_]+)/(?P<width>[\d]+)/(?P<height>[\d]+)/$',
        views.render_primary,
        name='avatar_render_primary'),
]
