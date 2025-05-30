from django.urls import path
from players import views

urlpatterns = [
    path("", views.list_players, name="list-players"),
    path("<int:pk>/detail/", views.detail_player, name="detail-player"),
]
