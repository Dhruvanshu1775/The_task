# Generated by Django 3.1.2 on 2021-02-24 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0003_auto_20210224_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='unit_price',
            new_name='product_price',
        ),
    ]
