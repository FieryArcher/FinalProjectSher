# Generated by Django 4.0.4 on 2022-05-12 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_order_orders_name_delete_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='waiter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to='data.waiter'),
        ),
    ]
