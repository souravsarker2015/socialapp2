from django.urls import path

from web_api.view import status_view

urlpatterns = [
    path('status/like/<int:id>', status_view.status_like, name='home'),
]
