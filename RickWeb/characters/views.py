from django.shortcuts import render
import requests as rq

def characters_view(request, *args, **kwargs):
    content = rq.get("https://rickandmortyapi.com/api/character")
    context = {'characters': content.content}
    return render(request, "characters.html", context)
