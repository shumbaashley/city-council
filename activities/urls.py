from django.urls import path

from . import views

app_name = 'activities'

urlpatterns = [
    path('forms/', views.get_name, name='index'),

]


# (r'^article/new/$', views.edit, {}, 'article_new'),
# (r'^article/edit/(?P<id>\d+)/$', views.edit, {}, 'article_edit'),