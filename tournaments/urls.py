from django.urls import path

from tournaments import views

urlpatterns = [
    path("", views.list_tournaments),
]
