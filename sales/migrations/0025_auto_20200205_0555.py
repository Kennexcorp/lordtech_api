# Generated by Django 2.2.7 on 2020-02-05 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0024_auto_20200205_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasales',
            name='cost',
            field=models.PositiveIntegerField(blank=True, default=123444),
            preserve_default=False,

        ),
        migrations.AlterField(
            model_name='datasales',
            name='total_mb',
            field=models.PositiveIntegerField(blank=True, default=11222),
            preserve_default=False,
        ),
    ]