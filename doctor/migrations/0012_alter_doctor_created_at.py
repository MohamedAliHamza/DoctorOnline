# Generated by Django 3.2.6 on 2022-04-05 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_alter_doctor_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 5, 21, 34, 31, 231485)),
        ),
    ]
