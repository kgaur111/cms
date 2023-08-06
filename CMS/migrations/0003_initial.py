# Generated by Django 4.1.7 on 2023-08-06 14:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CMS', '0002_remove_like_post_id_remove_like_user_id_delete_blog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=250)),
                ('Description', models.TextField()),
                ('Content', models.TextField()),
                ('Created_On', models.DateTimeField(auto_now_add=True)),
                ('Updated_On', models.DateTimeField(default=None, null=True)),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=100)),
                ('Contact_Details', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Liked_On', models.DateTimeField(default=datetime.datetime(2023, 8, 6, 20, 26, 17, 740670))),
                ('Post_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.blog')),
                ('User_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMS.user')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='Author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CMS.user'),
        ),
    ]
