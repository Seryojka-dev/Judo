from django.urls import path

from .views import index, team, photo, shedule, about, add_page, login, read_post

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('photo/', photo, name='photo'),
    path('shedule/', shedule, name='shedule'),
    path('post_list/', post_list, name='post_list'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', read_post, name='post')
]
