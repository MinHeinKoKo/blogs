# Generated by Django 4.0.4 on 2022-07-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0013_post_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(default=1, max_length=100000),
            preserve_default=False,
        ),
    ]
