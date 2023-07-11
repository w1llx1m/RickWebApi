from django.urls import path
from .views import characters_view, home_view

urlpatterns = [
    path('characters', characters_view, name='characters-view'),
    path('', home_view, name='home-view')
]