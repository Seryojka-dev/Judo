# Generated by Django 4.2.7 on 2023-12-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_category_rename_photo_postsphoto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]