from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

from django.contrib.auth import authenticate, login
from django.contrib import messages


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "users/login.html",
            context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        next_url = request.POST.get("next_url") or reverse("users:login")

        user = authenticate(
            username=username,
            password=password,
        )

        messages.add_message(
            request,
            messages.SUCCESS,
            settings.LOGIN_SUCCESS_MESSAGE,
        )

        if user:
            login(request, user)
            return redirect(next_url)

        return redirect(reverse("users:login"))
