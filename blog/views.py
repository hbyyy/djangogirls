from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def post_list(request):
    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post List!</h1>'
        '<div>'
        '<p>publish: 12.11.2019, 14:38</p>'
        '<h2><a href="">My First post</a></h2>'
        '<p>asdadasdasdasd</p>'
        '</div>'
        '<div>'
        '<p>published: 12.11.2019, 14.39</p>'
        '<h2><a href=">My second posy</a></h2>'
        '<p>adadlxxlxlxlxllx</p>'
        '</div>'
        '</body>'
        '</html>'
    )
