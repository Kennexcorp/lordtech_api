# Generated by Django 2.2.7 on 2019-12-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0013_create_data_Sales_summary_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasalessummary',
            name='actual_data_balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='datasalessummary',
            name='expected_data_balance',
            field=models.IntegerField(default=0),
        ),
    ]
