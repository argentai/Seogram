from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from django import forms

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SendEmail)
admin.site.register(Comment)
admin.site.register(Tag,TagAdmin)