from django.views.generic import View
from django.views.generic.edit import CreateView

from django.shortcuts import redirect, render
from posts.models import Post, Comment


class CommentBaseView(View):
    model = Comment


class PostCommentCreateView(CommentBaseView, CreateView):
    fields = [
        "content",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(
            id=self.kwargs.get("nickname"),
        )

        return super(PostCommentCreateView, self).form_valid(form)


def comments_edit(request, email, nickname):
    post = Post.objects.get(id=nickname)
    comment = post.comment_set.get(id=nickname)

    return render(
        request,
        "posts/comments_edit.html",
        {
            "post": post,
            "comment": comment,
        },
    )


def comments_update(request, email, nickname):
    post = Post.objects.get(id=nickname)
    comment = post.comment_set.get(id=nickname)

    content = request.POST.get("content")
    comment.content = content
    comment.save()

    return redirect(comment)


def comments_delete(request, email, nickname):
    post = Post.objects.get(id=nickname)
    comment = post.comment_set.get(id=nickname)

    comment.delete()
    return redirect(post)
