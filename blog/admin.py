from django.contrib import admin
from .models import Post
from users.models import Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)