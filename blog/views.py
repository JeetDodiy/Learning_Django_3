from django.shortcuts import render
from datetime import datetime


# Create your views here.
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def home(request):
    context = {
        "name": "rakesh C.",
        "age": 21,
        "skill": ['python', 'flutter', 'css'],
        "user": User("jeetu junjunvala", "rakesh"),
        "auther": None,
        "blog": {
            "title": 'blog',
            "content": ' this is bold',
            "create_at": datetime(2026, 7, 3, 11, 25)
        },
        "empty_value": None,
    }
    blogs = [{
        "title": "suke","content": "this is bold", "auther": True, "auther_name": "rakesh",},
        {"title": "nkara", "content": "this is heding", "auther": False , "auther_name": "suresh",},
        {"title": "kamchor", "content": "this is heding", "auther": False, "auther_name": "suresh", },
    ]
    return render(request, 'blog/home.html', {"contex": context, "blog": blogs})
