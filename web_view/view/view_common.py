from django.shortcuts import render


def render_path(request=None, path="home.html", context={}):
    context['html_file_path'] = path
    return render(request, 'include.html', context)
