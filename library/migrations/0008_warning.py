# Generated by Django 3.2 on 2021-04-24 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onreview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.review')),
            ],
        ),
    ]
