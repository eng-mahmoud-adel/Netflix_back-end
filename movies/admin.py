from django.contrib import admin
from .models import Movies
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','rate')

admin.site.register(Movies,MovieAdmin)
