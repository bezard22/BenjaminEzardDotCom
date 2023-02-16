from django.shortcuts import render
from os.path import join

from .models import Article

def index(request):
    articles = Article.objects.all()
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