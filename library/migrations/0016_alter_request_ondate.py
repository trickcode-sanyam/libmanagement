# Generated by Django 3.2 on 2021-04-25 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_request_ondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='ondate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
