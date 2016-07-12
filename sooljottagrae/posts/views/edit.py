from django.shortcuts import render

from posts.models import Post


def edit(request, post_id):
    return render(
        request,
        "posts/edit.html",
        {
            "post": Post.objects.get(id=post_id),
        }
    )

