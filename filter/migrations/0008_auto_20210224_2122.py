# Generated by Django 3.1.2 on 2021-02-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0007_auto_20210224_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product_price',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
    ]
