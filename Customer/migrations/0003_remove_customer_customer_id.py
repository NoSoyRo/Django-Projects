# Generated by Django 4.1.7 on 2023-02-28 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_customer_delete_tutorial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_id',
        ),
    ]