# Generated by Django 3.2 on 2021-04-25 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_alter_book_coverimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coverimg',
            field=models.ImageField(blank=True, null=True, upload_to='bookcovers/'),
        ),
    ]
