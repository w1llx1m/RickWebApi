from django.shortcuts import render
import json
import requests as rq

def home_view(request, *args, **kwargs):
    context = {}
    return render(request, "characters/home.html", context)

def characters_view(request, *args, **kwargs):
    content = get_all_characters()
    context = {'characters': content}
    return render(request, "characters/characters.html", context)


def get_all_characters():
    ret = rq.get("https://rickandmortyapi.com/api/character")
    jsonRet = json.loads(ret.content.decode('utf-8'))
    for x in jsonRet["results"]:
        pass
        #print(x["image"])
    return jsonRet