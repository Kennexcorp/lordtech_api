# Generated by Django 2.2.7 on 2019-12-09 07:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_create_data_Sales_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSalesSummary',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sales_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Start_airtime', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('Start_data', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('total_airtime_recieved', models.IntegerField(default=0)),
                ('total_direct_Sales', models.IntegerField(default=0)),
                ('total_sub_made', models.IntegerField(default=0)),
                ('expected_airtime', models.IntegerField(default=0)),
                ('actual_airtime', models.IntegerField(default=0)),
                ('total_data_shared', models.PositiveIntegerField()),
                ('no_order_treated', models.PositiveIntegerField()),
                ('outstanding', models.IntegerField(default=0)),
                ('is_closed', models.BooleanField(default=False)),
                ('sales_rep', models.ForeignKey(limit_choices_to={'category': 'da'}, on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='sales.SalesRep')),
            ],
            options={
                'verbose_name': 'Data Sales Summary',
                'verbose_name_plural': 'Data Sales Summaries',
            },
        ),
    ]
