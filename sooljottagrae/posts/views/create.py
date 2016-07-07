from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import render, redirect


class PostCreateFormView(View):
    
    def get(self, request, *args, **kwargs):
            return render(
                request,
                "posts/new.html",
                context={
                    #"post_id":post_id,
                    "title":title,
                    "content":content,
                    "image":image,
                },
            )


class PostCreateConfirmView(View):
   
    def get(self, request, *args, **kwargs):
        return redirect(revers("posts:create"))

    def post(self, request, *args, **kwargs):
        #post_id = request.POST.get("post_id")
        title = request.POST.get("title")
        image = request.POST.get("image")
        content = request.POST.get("content")

        return render(
            request,
            "posts/confirms.html",
            context={},
        )

 

