# Generated by Django 4.2.7 on 2023-11-29 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0007_item_completed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='workshop.item'),
        ),
    ]
