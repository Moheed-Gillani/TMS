# Generated by Django 3.2 on 2021-04-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_post_orders_customer_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_orders',
            name='shipping_address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
