from django.shortcuts import get_object_or_404, render, redirect
from blog.forms import CreatePostForm
from blog.forms import Post

def home(request):
    posts = Post.objects.all().order_by('-id')
    selected_post = None

    # Check if a blog was clicked (via ?blog_id=123 in the URL)
    blog_id = request.GET.get("blog_id")
    if blog_id:
        selected_post = get_object_or_404(Post, id=blog_id)
    else:
        selected_post = None
        
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'blog/home.html', {
        'form': form,
        'posts': posts,
        'selected_post': selected_post,
    })