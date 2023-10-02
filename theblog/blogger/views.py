from django.shortcuts import render, redirect

from blogger.forms import PostModelForm
from blogger.models import Post
# Create your views here.
from django.shortcuts import get_object_or_404

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.likes += 1
        post.save()
    context = {"post": post}
    return render(request, "post_detail.html", context=context)

def start_page(request):
    context = {"blogs":Post.objects.all()}
    return render(request, "index.html", context=context)


def add_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("start_page")

    else:
        form = PostModelForm()

    context = {"form": form}
    return render(request, "add_post.html", context=context)