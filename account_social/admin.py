from django.contrib import admin
from account_social.models import Profile


class ContentAdmin(admin.ModelAdmin):
    list_display = ['user','about_me', 'photo',]
    list_filter = ['user']


admin.site.register(Profile, ContentAdmin)
