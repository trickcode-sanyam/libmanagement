# Generated by Django 3.2 on 2021-04-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20210425_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='coverimg',
            field=models.ImageField(null=True, upload_to='bookcovers/'),
        ),
    ]