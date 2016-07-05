from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

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
        email = request.POST.get("email")

        next_url = request.POST.get("next_url") or reverse("login")

        user = authenticate(
            username=username,
            password=password,
            email=email,
        )

        if user:
            login(request, user)
            return redirect(next_url)

        return redirect(reverse("login"))
