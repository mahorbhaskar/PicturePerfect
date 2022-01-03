from django.urls import path
from .views import (
    hello_world_view,
    post_list_and_create,
)

app_name = 'posts'

urlpatterns = [
    path('',post_list_and_create, name='main'),
    path('hello-world/',hello_world_view,name='hello-world'),
]