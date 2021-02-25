from django.contrib import admin
from .models import Post, Comment, Likes, Views, Twister
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    list_display_links = ('title',)
    search_fields = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','post', 'created')
    list_display_links = ('author',)
    search_fields = ('author',)

@admin.register(Twister)
class TwisterAdmin(admin.ModelAdmin):
    list_display = ('author','id', 'created')
    list_display_links = ('author',)
    search_fields = ('author',)

@admin.register(Views)
class ViewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    list_display_links = ('user',)
    search_fields = ('user',)

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    list_display_links = ('user',)
    search_fields = ('user',)
