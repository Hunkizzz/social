# Generated by Django 2.1.3 on 2019-02-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_social', '0012_auto_20181110_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite_articles',
            field=models.ManyToManyField(blank=True, related_name='favorite_articles', to='social_content.Content'),
        ),
    ]
