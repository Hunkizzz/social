# Generated by Django 2.0.5 on 2018-08-05 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_content', '0004_auto_20180805_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='users_like',
            new_name='user_like',
        ),
    ]
