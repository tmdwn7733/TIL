# Generated by Django 5.0.1 on 2024-03-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(to='tag.tag', verbose_name='태그'),
        ),
    ]