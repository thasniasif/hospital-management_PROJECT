# Generated by Django 4.1.5 on 2023-09-07 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0016_alter_discharge_tb_p_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discharge_tb',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='hospitalapp.patient'),
        ),
    ]
