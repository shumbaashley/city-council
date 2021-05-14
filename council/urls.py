from django.urls import path

from . import views

app_name = 'council'

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("activities", views.activities, name="activities"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile", views.profile, name="profile"),
    path("work-plans/", views.work_plans, name="work-plans"),
    path("performance", views.performance, name="performance"),
    path('edit-review/<int:id>/', views.review_edit, {}, 'review_edit'),
    path('review/<int:id>/delete', views.delete_view, 'delete_view'),

]