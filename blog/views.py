from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.filter(active=True, important=True)[0:3]
    return render(request, 'accounts/template1.html', {'posts': posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'accounts/template2.html', {'posts': posts})
   
def contact(request):
    return render(request, 'accounts/template4.html')


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'accounts/post.html', {'post': post})      






    