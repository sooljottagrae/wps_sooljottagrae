from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PostNewView(LoginRequiredMixin, TemplateView):
    template_name = "posts/new.html"
