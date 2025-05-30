from django.shortcuts import render, redirect
from blog.forms import CreatePostForm
from blog.forms import Post

def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        print(f'request:{request}')
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'blog/home.html', {'form': form, 'posts': posts})