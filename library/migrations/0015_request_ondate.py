# Generated by Django 3.2 on 2021-04-25 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_auto_20210425_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='ondate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
