# Generated by Django 4.0.4 on 2022-07-17 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0009_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
