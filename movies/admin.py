from django.contrib import admin
from .models import Movies , Writer,Genre,Actors
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','rate')

admin.site.register(Movies,MovieAdmin)
admin.site.register(Writer)
admin.site.register(Genre)
admin.site.register(Actors)
