# Generated by Django 4.2.7 on 2023-11-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0006_remove_item_delivered_by_item_district_item_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
