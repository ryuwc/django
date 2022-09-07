from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods


@login_required
@require_http_methods(['GET', 'POST'])
def detail(request,pk):
    chatting = get_object_or_404(Chat,pk=pk)
    context = {
        'chatting':chatting,
    }
    return render(request,'chattings/detail.html',context)