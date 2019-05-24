from django.contrib import admin
from social_content.models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','slug', 'image', 'created',]
    list_filter = ['created']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Content, ContentAdmin)

# Register your models here.
