# Generated by Django 2.2.7 on 2020-02-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0025_auto_20200205_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataplan',
            name='cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dataplan',
            name='mb',
            field=models.FloatField(),
        ),
    ]