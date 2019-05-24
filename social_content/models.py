from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from pytils.translit import slugify
from tinymce.models import HTMLField


class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='content_created', on_delete=models.CASCADE);
    title = models.CharField(max_length=180, unique=True, verbose_name='Введите заголовок')
    slug = models.SlugField(max_length=220, db_index=True, verbose_name='slug')
    image = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, default='no_image_app_content.png', verbose_name='Загрузить изображение')
    entry = HTMLField(blank=True, verbose_name='Запись')
    created = models.DateTimeField(auto_now_add=True)
    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='content_liked', blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Content, self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('social_content:detail', kwargs={'id':self.id, 'slug':self.slug})

    def __str__(self):
        return self.title


# Create your models here.
