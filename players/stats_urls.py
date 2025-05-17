from django.urls import path

from players import views

urlpatterns = [
    path("", views.all_stats),
]
