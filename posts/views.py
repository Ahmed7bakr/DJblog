from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    objects = Post.objects.all()
    return render(request,'posts.html',{'posts':objects})

def post_detail(request,id):
    single = Post.objects.get(id=id)
    return render (request,'post_detail.html',{'post':single})


def new_post(request):
    if request.method == 'POST':
      form = PostForm(request.POST,request.FILES)
      if form.is_valid():
          form.save()
    else:
        form = PostForm()
    return render(request,'new.html',{'form':form})

