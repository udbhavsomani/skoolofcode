# Generated by Django 4.0 on 2021-12-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_availabletiming_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabletiming',
            name='data',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
