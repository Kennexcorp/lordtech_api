# Generated by Django 2.2.7 on 2019-12-10 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0019_create_trade_summary_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trade',
            options={'verbose_name': 'Trade', 'verbose_name_plural': 'Trades'},
        ),
        migrations.AlterModelOptions(
            name='tradesummary',
            options={'verbose_name': 'Trade Sales Summary', 'verbose_name_plural': 'Trade Sales Summaries'},
        ),
        migrations.RenameField(
            model_name='tradesummary',
            old_name='actual_balance',
            new_name='balance',
        ),
        migrations.RemoveField(
            model_name='tradesummary',
            name='expected_balance',
        ),
        migrations.RemoveField(
            model_name='tradesummary',
            name='outstanding',
        ),
    ]
