# Generated by Django 4.1 on 2022-09-28 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appinicio', '0004_post_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.CharField(default='vino de buen cupero....', max_length=400),
        ),
    ]
