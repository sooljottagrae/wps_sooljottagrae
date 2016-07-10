from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import render, redirect


class PostCreateFormView(View):

    def get(self, request, *args, **kwargs):
            return render(
                request,
                "posts/new.html",
                context={
                    "title": title,
                    "content": content,
                    "image": image,
                },
            )


class PostCreateConfirmFormView(View):

    def get(self, request, *args, **kwargs):
        return redirect(revers("posts:create"))

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        image = request.POST.get("image")
        content = request.POST.get("content")

        return render(
            request,
            "posts/confirm.html",
            context={},
        )
