from django.urls import path
from .views import characters_view

urlpatterns = [
    path('characters', characters_view, name='characters-view')
]