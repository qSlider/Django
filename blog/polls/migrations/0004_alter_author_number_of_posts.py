# Generated by Django 5.1.1 on 2024-10-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_author_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='number_of_posts',
            field=models.IntegerField(default=0),
        ),
    ]
