from django.urls import path
from apis.views import SongListView

urlpatterns = [
    path('song/', SongListView.as_view(),name="song"),
    path('add-rating/<str:song_id>/',SongListView.as_view(),name="add-rating")
]