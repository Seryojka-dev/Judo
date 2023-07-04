<<<<<<< HEAD
# Generated by Django 2.2.19 on 2023-07-02 16:04

from django.db import migrations, models
import django.db.models.deletion
=======
# Generated by Django 2.2.19 on 2023-07-04 18:32

from django.db import migrations, models
>>>>>>> 5f7335b3241fad5b030fe7a203a90fa7fc2cc9c8


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Посты',
                'verbose_name_plural': 'Посты',
                'ordering': ['time_create', 'title'],
            },
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='backend.Posts')),
            ],
            options={
                'verbose_name': 'Коментарии',
                'verbose_name_plural': 'Коментарии',
                'ordering': (['created'],),
            },
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['created'], name='backend_com_created_10a4a2_idx'),
        ),
=======
>>>>>>> 5f7335b3241fad5b030fe7a203a90fa7fc2cc9c8
    ]
