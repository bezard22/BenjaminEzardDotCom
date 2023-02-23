from django.shortcuts import render
from django.http import JsonResponse
from os.path import join, split

from .models import Article
import sys
sys.path.append(join(split(sys.path[0])[0], "articles"))
import importlib

def index(request):
    articles = Article.objects.filter(isPublished=1)
    return render(request, 'portfolio/index.html', {"articles": articles})

def article(request, article):
    baseDir = join(f"site_{article}","static")
    articleObj = Article.objects.filter(name=article)[0]
    return render(request, 'portfolio/article.html', {
        "article": article,
        "articleObj": articleObj,
        "stylesheet": join(baseDir,"style.css"),
        "articleFile": join(baseDir,"index.html"),
        "scriptFile": join(baseDir,"index.js"),
    })

def articleAPI(request, article):
    if request.method == "GET":
        api = importlib.import_module("articles.site_affineCipher.src.api")
        return JsonResponse(api.call(**request.GET.dict()))