from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_POST, require_http_methods

@require_POST
def delete(request,pk):
    if request.user.is_authenticated:
        chatting = get_object_or_404(Chat,pk=pk)
        chatting.delete()
    return redirect("chattings:index")