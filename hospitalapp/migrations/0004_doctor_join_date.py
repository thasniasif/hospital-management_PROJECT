# Generated by Django 4.1.5 on 2023-08-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_doctor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='join_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Created'),
        ),
    ]
