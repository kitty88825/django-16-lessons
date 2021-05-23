from django.contrib import admin

from .models import Mood, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)


admin.site.register(Mood)
admin.site.register(Post, PostAdmin)
