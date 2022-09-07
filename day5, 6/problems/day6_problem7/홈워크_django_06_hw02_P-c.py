from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST,request.FILES)
        if form.is_valid:
            chatting = form.save()
            return redirect('chattings:detail',chatting.pk)
    else:
        form = ChatForm()
    context={
        'form':form
    }
    return render(request,'chattings/create.html',context)
