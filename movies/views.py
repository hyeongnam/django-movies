from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from .models import Movie


@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET','POST'])
def new(request):
    # GET
    if request.method == 'GET':
        return render(request, 'movies/new.html')
    # POST
    else:
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie = Movie(title=title, title_origin=title_origin, vote_count=vote_count,
                      open_date=open_date, genre=genre, score=score, poster_url=poster_url,
                      description=description)
        movie.save()
        return redirect('movies:detail', movie.id)


@require_GET
# movie_id 에 맞는 movie 데이터를 넘겨줘야 함
def detail(request, movie_id): # /movies/3/
    movie = get_object_or_404(Movie, id=movie_id)
    context = {'movie': movie}
    return render(request, 'movies/detail.html',context)


@require_POST
def delete(request, movie_id):
    if request.method == 'GET':
        return redirect('movies:detail',movie_id)
    else:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return redirect('movies:index')


@require_http_methods(['GET','POST'])
def edit(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        context = {'movie': movie}
        return render(request, 'movies/edit.html', context)
    else:
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie.title = title
        movie.title_origin = title_origin
        movie.vote_count = vote_count
        movie.open_date = open_date
        movie.genre = genre
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description
        movie.save()
        # detail page 로 redirect 한다.
        return redirect('movies:detail', movie_id)
