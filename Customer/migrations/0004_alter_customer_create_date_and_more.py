# Generated by Django 4.1.7 on 2023-02-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_remove_customer_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_update',
            field=models.CharField(max_length=2000),
        ),
    ]
