from django.contrib import admin
from applications.musics.models import *

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Song)