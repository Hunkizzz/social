from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from social_content.models import Content



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about_me = models.TextField(blank=True, max_length=160, help_text="Максимум 160 символов.")
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True, default='no_image_app_content.png')
    favorite_articles = models.ManyToManyField(Content, related_name='favorite_articles', blank=True)



    def __str__(self):
        return "Мой профиль {}".format(self.user.username)
