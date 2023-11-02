from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from .forms import MoviesForm


def create(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        #data = """{"1": {"name": "what", "year": "2012", "actors": "actors"}, "2": {"name": "hi", "year": "2002", "actors": "actor5"}, "3": {"name": "hi", "year": "2002", "actors": "actor5"}}"""
        #print(maxID(json.loads(data)))
        #print(json.loads(data))
        # create a form instance and populate it with data from the request:
        form = MoviesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            response = redirect("list")
            #maxID(json.loads(request.COOKIES['movie_list']))
            if 'movie_list' not in request.COOKIES:
                response.set_cookie("movie_list",{})
                return response
                #print(request.COOKIES)
            print(request.COOKIES["movie_list"])
            formData = {
            'name': request.POST['name'],
                'year': request.POST['year'],
                'actors': request.POST['actors']}
            newData = json.loads(request.COOKIES['movie_list'])
            newData[maxID(json.loads(request.COOKIES['movie_list']))] = formData
            response.set_cookie(key="movie_list",value=json.dumps(newData))
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return response
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MoviesForm()
    return render(request, "movies/form.html", {"form": form})

def list(request):
    print("this is running")
    movie_cookies = request.COOKIES
    movie_list = {}
    response = render(request, "movies/cookies.html")
    if 'movie_list' in movie_cookies:
        return render(request, "movies/cookies.html", context={'movie_list': request.COOKIES['movie_list']})
    else:
        response.set_cookie(key="movie_list", value=movie_list)
        return render(request, "movies/cookies.html", context={'movie_list': movie_list})

def maxID(list):
    if len(list) == 0:
        return 1
    ids = []
    for element in reversed(list):
        for key in element:
            ids.append(int(key))
    return max(ids)+1

# Create your views here.
