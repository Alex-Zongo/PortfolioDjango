from django.shortcuts import render, HttpResponse
from blog.models import Post, Comment, Category
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    # posts = paginator.get_page(page)

    try:
        psts = paginator.page(page)
    except PageNotAnInteger:
        psts = paginator.page(1)
    except EmptyPage:
        psts = paginator.page(paginator.num_pages)

    context = {
        "posts": psts,
        "page": page
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post)
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }

    return render(request, "blog_detail.html", context)
