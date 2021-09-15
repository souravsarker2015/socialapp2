from django.shortcuts import render

from web_api.models import Status
from web_view.view.view_common import render_path


def all_test(request):
    status_list = Status.objects.all().order_by('-pk')
    return render(request, 'test.html', {'status_list': status_list})


def home_page(request):
    status_list = Status.objects.all().order_by('-pk')
    return render_path(request, 'home.html', {"status_list": status_list})


def username_page(request):
    status_list = Status.objects.all().order_by('-pk')
    return render_path(request, 'page/page.html', {"status_list": status_list})
