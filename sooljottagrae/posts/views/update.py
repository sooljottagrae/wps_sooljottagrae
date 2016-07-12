from django.shortcuts import redirect

from posts.models import Post


def update(request, post_id):
    post = Post.objects.get(id=post_id)
    title = request.POST.get("title")
    content = request.POST.get("content")
    image = request.Post.get("image")

    post.title = title
    post.content = content
    post.image = image
    post.save()
    
    return redirect(post)

