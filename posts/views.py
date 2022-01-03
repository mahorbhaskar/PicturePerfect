from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
# Create your views here.
def post_list_and_create(request):
    qs = Post.objects.all()
    return render(request,'posts/main.html',{'qs':qs})

def hello_world_view(request):
    return JsonResponse({'text':'This is my Response text from hellow world views'})