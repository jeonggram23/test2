from django.shortcuts import render, redirect
from .models import Post, Comment
from .form import PostForm, CommentForm

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)


def detail(request, id):

    post = Post.objects.get(id=id)
    comment_form = CommentForm()

    comment_list = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comment_form': comment_form,
        'comment_list': comment_list,
    }

    return render(request, 'detail.html', context)


def create(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
        
    else:
        form = PostForm()

    context = {
        'form':form
    }

    return render(request, 'form.html', context)


def comment_create(request, post_id):
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)

        comment.post_id = post_id

        comment.save()

        return redirect('posts:detail', id=post_id)