# Generated by Django 5.0.3 on 2024-05-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_posts_latitude_remove_posts_longitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='posts',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]