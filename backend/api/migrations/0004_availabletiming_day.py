# Generated by Django 4.0 on 2021-12-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_availabletiming'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabletiming',
            name='day',
            field=models.CharField(default='Monday', max_length=10),
        ),
    ]
