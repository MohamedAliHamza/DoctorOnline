# Generated by Django 3.2.6 on 2022-03-14 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_remove_clinicduration_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicduration',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.doctor', verbose_name='Doctor'),
            preserve_default=False,
        ),
    ]
