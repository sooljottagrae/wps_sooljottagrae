from django.contrib import messages
from django.contrib.auth import logout

from django.conf import settings
from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            settings.LOGOUT_SUCCESS_MESSAGE,
        )
        return redirect(reverse("users:login"))
