# Generated by Django 3.1.7 on 2021-03-16 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('ci', models.CharField(max_length=10, unique=True, verbose_name='Ci')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Fecha de creacion')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='cvitae/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
    ]
