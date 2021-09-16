from django.contrib import admin
from django.db import models
from .models import Category, Persons, Genre, Movie, MovieShoots, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)

class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    fieldsets = (
        (None,{
            'fields': (('title', 'tagline'), )
        }),
        (None,{
            'fields': ('description', 'poster')
        }),
        (None,{
            'fields': (('year', 'world_premiere', 'country'), )
        }),
        ('Persons',{
            'classes': ('collapse',),
            'fields': (('actors', 'directors', 'genres', 'category'), )
        }),
        (None,{
            'fields': (('budget', 'feels_in_usa', 'feels_in_world'), )
        }),
        ('Options',{
            'fields': (('url', 'draft'), )
        }),
    )

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip',)

@admin.register(MovieShoots)
class MovieShootsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie')


admin.site.register(RatingStar)

