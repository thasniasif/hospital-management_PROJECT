# Generated by Django 4.1.5 on 2023-09-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0019_discharge_tb_room_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='discharge_tb',
            name='doc_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='discharge_tb',
            name='medicine_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='discharge_tb',
            name='other_charge',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='discharge_tb',
            name='total_charge',
            field=models.IntegerField(default=0),
        ),
    ]
