from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie
from .models import Review

def home(request):
    movies=Movie.objects.all()
    return render(request, 'movies/home.html',{'movies':movies})

def movie_details(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id) # URL den gelen id ye göre ilgili filmi veri tabanından çekeceğiz
    reviews=movie.reviews.all()

    if request.method == 'POST':
        comment=request.POST.get('comment')
        rating=request.POST.get('rating')

        if comment and rating:
            Review.objects.create(
                movie=movie,
                comment=comment,
                rating=rating
                )
            return redirect('home')
    context = {
        'movie': movie,
        'reviews': reviews,
    }
    
    return render(request, 'movies/movie_details.html', context)     

# get_object_or_404 --> Verilen kritere göre modelden nesne alır yoksa 404 hatası verir        