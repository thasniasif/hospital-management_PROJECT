# Generated by Django 4.1.5 on 2023-09-15 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0022_doctor_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='token',
        ),
    ]
