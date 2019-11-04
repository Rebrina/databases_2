from django.views.generic import ListView
from django.shortcuts import render
from .models import Article, Membership, Scope 

def articles_list(request):
    template = 'articles/news.html'
    context = {}
    ordering = '-published_at'

    articles = Article.objects.all()
    context['tags'] = {}
    for article in articles:
        context['tags'][article.id] = {}
        tags = Scope.objects.filter(article=article.id).order_by('-membership__is_main', 'tematik').all()
        context['tags'][article.id] = tags
    context['object_list'] = Article.objects.all()

    return render(request, template, context)
