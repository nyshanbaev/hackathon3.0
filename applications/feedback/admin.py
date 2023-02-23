from django.contrib import admin
from applications.feedback.models import *

admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Feedback)

