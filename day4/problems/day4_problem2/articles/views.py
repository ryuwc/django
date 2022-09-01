from urllib.request import Request
from django.shortcuts import render, redirect

import articles
from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    # articles = Article.objects.all()[::-1]    # 최신글부터
    articles = Article.objects.order_by('-pk')  # 내림차순 order_by('-pk')
    context = {
        'articles': articles
    }
    
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)
    
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
