# Generated by Django 4.1.7 on 2023-08-06 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='Post_Id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='User_Id',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
