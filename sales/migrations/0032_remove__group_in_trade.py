# Generated by Django 2.2.7 on 2020-03-01 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0031_add__trade_group__to_trade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='group',
        ),
    ]
