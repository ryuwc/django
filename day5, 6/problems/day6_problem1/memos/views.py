from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .models import Memo
from .forms import MemoForm

# Create your views here.
@require_safe
def index(request):
    memos = Memo.objects.all
    context = {
        'memos': memos,
    }
    return render(request, 'memos/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save()
            # return redirect('memos:detail', memo.pk)
            return redirect('memos:index')
    else:
        form = MemoForm()
    context = {
        'form': form,
    }
    return render(request, 'memos/create.html', context)

@require_safe
def detail(request, pk):
    memos = Memo.objects.get(pk=pk)
    context = {
        'memos': memos
    }
    return render(request, 'memos/detail.html', context)

def delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memos:index')