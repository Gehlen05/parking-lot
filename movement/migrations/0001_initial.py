# Generated by Django 2.2.9 on 2022-06-06 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0002_auto_20220605_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField()),
                ('exit_date', models.DateTimeField(null=True)),
                ('validate_date', models.DateTimeField(null=True)),
                ('value_real', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('plate', models.CharField(max_length=50)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.Vehicle')),
            ],
            options={
                'db_table': 'TB_PARKMOVEMENT',
            },
        ),
    ]
