# Generated by Django 3.2 on 2021-04-26 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='shop_address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
