from django.urls import path

from web_view.view import views_auth, views_post

urlpatterns = [
    path('', views_auth.home, name='home'),
    path('test', views_post.all_test, name='test'),
    path('join', views_auth.sign_in_up, name='signup'),
    path('login', views_auth.sign_in_up, name='login'),
    path('logout', views_auth.log_out, name='logout'),
    path('logout/', views_auth.log_out, name='logout'),

    path('<str:username>', views_post.username_page, name='username_page'),
]
