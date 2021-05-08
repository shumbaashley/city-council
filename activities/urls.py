from django.urls import path

from . import views

app_name = 'activities'

urlpatterns = [
    path('forms/', views.get_name, name='index'),

]