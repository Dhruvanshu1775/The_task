# Generated by Django 3.1.2 on 2021-02-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0014_auto_20210224_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
    ]
