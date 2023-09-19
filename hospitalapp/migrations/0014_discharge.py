# Generated by Django 4.1.5 on 2023-09-07 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0013_appointment_doctor_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='discharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_user_name', models.CharField(blank=True, max_length=200)),
                ('release_date', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.patient')),
            ],
        ),
    ]
