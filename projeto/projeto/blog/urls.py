from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home/', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^new/', views.post_new),
    url(r'^$', views.logar),
    url(r'user_new/', views.user_new),
    url(r'^post/(?P<pk>[0-9]+)/edit', views.post_edit),
    url(r'^post/(?P<pk>[0-9]+)/delete', views.post_delete),
    url(r'logout', views.sair),

]