from django.shortcuts import render

import throw_catch

# Create your views here.
def first(request):
    
    return render(request, 'throw_catch/first.html')

def second(request):
    value = request.GET.get('throw'),
    context = {
        'value': value,
    }
    return render(request, 'throw_catch/second.html', context)
