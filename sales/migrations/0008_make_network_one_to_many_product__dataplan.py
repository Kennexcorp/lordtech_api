# Generated by Django 2.2.7 on 2019-12-01 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_create_dataplan_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataplan',
            name='network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Product'),
        ),
    ]