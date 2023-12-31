# Generated by Django 4.1.5 on 2023-09-07 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0017_alter_discharge_tb_p_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='discharge_tb',
            name='doctor_user_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='discharge_tb',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.patient'),
        ),
    ]
