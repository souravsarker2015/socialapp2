from django.contrib import auth
from django.shortcuts import redirect

from web_view.view.view_common import render_path
from web_view.view.views_post import home_page


def home(request):
    if request.user.is_anonymous:
        return sign_in_up(request)
    return home_page(request)


def sign_in_up(request):
    if not request.user.is_anonymous:
        return redirect("/")
    return render_path(request, 'login.html', {})


def log_out(request):
    auth.logout(request)
    return redirect("/")
