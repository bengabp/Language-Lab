# Generated by Django 4.1.4 on 2023-01-06 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0004_alter_friendrequest_from_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
