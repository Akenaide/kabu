from django.urls import path

from tournaments import views

urlpatterns = [
    path("tournaments/", views.list_tournaments),
    path("seasons/", views.list_seasons),
    path("seasons/<int:pk>/", views.detail_season, name="season-detail"),
]
