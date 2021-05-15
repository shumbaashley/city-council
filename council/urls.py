from django.urls import path

from . import views

app_name = 'council'

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile, name="profile"),
    path('delete-performance-review/<int:id>/delete', views.delete_view, 'delete_view'),
    path('edit-performance-review/<int:review_id>/', views.edit_performance_review, name="edit_performance_review"),
    path('create-performance-review/', views.create_performance_review, name="create_performance_review"),
]