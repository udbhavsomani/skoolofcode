# Generated by Django 4.0 on 2021-12-19 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_availabletiming_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availabletiming',
            name='day',
        ),
        migrations.RemoveField(
            model_name='availabletiming',
            name='e_n',
        ),
        migrations.RemoveField(
            model_name='availabletiming',
            name='e_t',
        ),
        migrations.RemoveField(
            model_name='availabletiming',
            name='n_t',
        ),
        migrations.RemoveField(
            model_name='availabletiming',
            name='o_t',
        ),
        migrations.RemoveField(
            model_name='availabletiming',
            name='t_e',
        ),
        migrations.RemoveField(
            model_name='availabletiming',
            name='t_o',
        ),
        migrations.RemoveField(
            model_name='availabletiming',
            name='t_th',
        ),
    ]
