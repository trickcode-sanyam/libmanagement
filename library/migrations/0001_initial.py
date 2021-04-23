# Generated by Django 3.2 on 2021-04-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('isbn', models.CharField(max_length=20)),
                ('avl', models.BooleanField()),
                ('booknum', models.IntegerField()),
            ],
        ),
    ]
