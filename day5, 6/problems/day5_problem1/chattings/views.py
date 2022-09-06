from django.shortcuts import render, redirect
from .models import Chat

# Create your views here.
def index(request):
    chattings = Chat.objects.all()
    context = {
        'chattings': chattings,
    }
    return render(request, 'chattings/index.html', context)

def new(request):
    return render(request, 'chattings/new.html')

def create(request):
    user = request.POST.get('user')
    content = request.POST.get('content')

    chatting = Chat(user=user, content=content)
    chatting.save()
    return redirect('chattings:detail', chatting.pk)

def detail(request, pk):
    chatting = Chat.objects.get(pk=pk)
    context = {
        'chatting': chatting
    }
    return render(request, 'chattings/detail.html', context)

