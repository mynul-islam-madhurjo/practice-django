from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_world(request, *args, **kwargs):
    # print(request.user)

    # return HttpResponse("<html><body><h1>Hello, World!</h1></body></html>")
    my_conext = {
        'my_text': 'This is about us',
        'my_number': 123,
        'lists': [10,20,30],
        'title':'this is the title',
        'comment': '<h1>This is a comment</h1>'
    }
    return render(request, 'home.html', my_conext)
