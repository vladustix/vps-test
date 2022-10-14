from django.urls import path

from .views import (
    ServerListView,
    ServerSingleView,
)


urlpatterns = [
    path('', ServerListView.as_view()),
    path('<int:uid>', ServerSingleView.as_view())
]
