from django.contrib import admin

# Register your models here.
from .models import Recipe

admin.site.register(Recipe)


# @admin.register(Post)
# class CustomUserAdmin(admin.ModelAdmin):
#   list_display = ['author', 'id', 'content', ]