# Generated by Django 3.0.8 on 2020-07-18 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='date_published',
            new_name='published_year',
        ),
    ]
