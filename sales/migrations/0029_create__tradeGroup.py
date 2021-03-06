# Generated by Django 2.2.7 on 2020-03-01 10:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0028_add__order_id_to_trade'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeGroup',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('balance', models.PositiveIntegerField()),
                ('selling_currency', models.CharField(choices=[('naira', 'naira'), ('yuan', 'yuan')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
