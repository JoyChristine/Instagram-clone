# Generated by Django 4.0.4 on 2022-06-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_follow_remove_postimage_post_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]