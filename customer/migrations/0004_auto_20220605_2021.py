# Generated by Django 2.2.9 on 2022-06-05 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20220605_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='sobrenome',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='TB_CUSTOMER',
        ),
    ]
