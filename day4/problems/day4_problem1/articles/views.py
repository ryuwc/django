from django.shortcuts import render
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
    return render(request, 'articles/create.html')

