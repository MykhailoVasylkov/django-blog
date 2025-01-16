from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

"""
Register Post model in admin panel.
Add how post list is displaying.
Add search functionality.
Add filter functionality.
Add prepopulated filds directly to add post page.
Add summernote functionality to content field.
"""
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
