# the first View
'''from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hi There!')'''

# the second View
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    ret = '<body>'
    all_posts = Post.objects.all()
    for post in all_posts:
        ret = ret + '<p>' + post.text + '</p>'
    ret = ret + '</p>'

    return HttpResponse(ret)