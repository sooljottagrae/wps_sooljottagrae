from django import forms

from .post import Post


class PostForm(forms.ModelsForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
