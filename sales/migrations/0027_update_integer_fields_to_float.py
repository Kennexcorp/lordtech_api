# Generated by Django 2.2.7 on 2020-02-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0026_make__mb_cost_float_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airtimereceived',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cashreceived',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='datasales',
            name='cost',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='datasales',
            name='total_mb',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='datasalessummary',
            name='actual_airtime',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datasalessummary',
            name='actual_data_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datasalessummary',
            name='expected_airtime',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datasalessummary',
            name='expected_data_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datasalessummary',
            name='outstanding',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='datasalessummary',
            name='total_airtime_received',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datasalessummary',
            name='total_data_shared',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='datasalessummary',
            name='total_direct_Sales',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='datasubscription',
            name='cost_per_sub',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='datasubscription',
            name='mb_per_sub',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='profit',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salesrep',
            name='airtime_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='salesrep',
            name='cash_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='salesrep',
            name='data_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='trade',
            name='amount_paid',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='buying_rate',
            field=models.FloatField(verbose_name='Buying rate (Naira)'),
        ),
        migrations.AlterField(
            model_name='tradesummary',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='tradesummary',
            name='total_cash_received',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='tradesummary',
            name='total_cash_used',
            field=models.FloatField(default=0.0),
        ),
    ]
