from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Chat

# Create your views here.
@require_safe
def index(request):
    chattings = Chat.objects.all()
    context = {
        'chattings': chattings,
    }
    return render(request, 'chattings/index.html', context)


def new(request):
    return render(request, 'chattings/new.html')

@require_http_methods(['GET', 'POST'])
def create(request):
    user = request.POST.get('user')
    content = request.POST.get('content')

    chatting = Chat(user=user, content=content)
    chatting.save()
    return redirect('chattings:detail', chatting.pk)

@require_safe
def detail(request, pk):
    chatting = Chat.objects.get(pk=pk)
    context = {
        'chatting': chatting
    }
    return render(request, 'chattings/detail.html', context)

@require_POST
def delete(request, pk):
    chatting = Chat.objects.get(pk=pk)
    chatting.delete()
    return redirect('chattings:index')


