# Generated by Django 4.0.4 on 2022-07-12 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0005_alter_comment_name_alter_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]