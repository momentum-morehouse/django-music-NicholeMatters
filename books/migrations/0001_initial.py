# Generated by Django 3.0.8 on 2020-07-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('book_title', models.CharField(max_length=255)),
                ('date_published', models.DateField()),
                ('book_cover', models.TextField(blank=True, null=True)),
                ('chapter_list', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
