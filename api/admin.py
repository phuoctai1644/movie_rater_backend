from django.contrib import admin
from .models import Movie, Rating, User

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(User)
