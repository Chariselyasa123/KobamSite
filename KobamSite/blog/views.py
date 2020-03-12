from django.shortcuts import render, get_object_or_404
from .models import Post 
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
# Create your views here.
@login_required
def about(request):
    return render(request, 'blog/base.html')

@login_required
def materi_cpp_pendahuluan(request):

    context={
        'posts':Post.objects.filter(pk=1)
    }
    return render(request, 'blog/materi_cpp_pendahuluan.html', context)

@login_required
def menu_materi(request):
    return render(request, 'blog/menu_materi.html')
