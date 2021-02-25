from django.contrib import admin
from .models import Profile
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birthday', 'created')
    list_display_links = ('user',)
    search_fields = ('user',)
    prepopulated_fields = {'slug': ('user',)}
