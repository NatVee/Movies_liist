from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def v(request):
    d = request.GET

    try:
        if 'del' in d:
            m = Movie.objects.get(id=int(d['del']))
            m.delete()

        else:
            if str(d['title_data']) != str(Movie.objects.latest()):
                m = Movie(title=d['title_data'], year=d['year_data'])
                m.save()
    except:
        print('No query')

    posts = Movie.objects.all()
    return render(request, 'movies/base.html', {'posts': posts})



