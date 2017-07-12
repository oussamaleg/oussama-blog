from django.contrib import admin
from technology.models import Blog, Part, Profile

admin.site.register(Part)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'publisher','part')

admin.site.register(Blog, BlogAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
admin.site.register(Profile, ProfileAdmin)
