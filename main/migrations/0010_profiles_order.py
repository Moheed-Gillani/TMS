# Generated by Django 3.2 on 2021-04-28 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_post_orders_shipping_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='profiles_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50, null=True)),
                ('customer_email', models.EmailField(max_length=254, null=True)),
                ('customer_contact', models.IntegerField(null=True)),
                ('shipping_address', models.CharField(max_length=100, null=True)),
                ('to_tailor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profiles')),
            ],
        ),
    ]
