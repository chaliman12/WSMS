# Generated by Django 4.2.7 on 2023-11-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(auto_created=True, choices=[('pending', 'pending'), ('Damage', 'Damage'), ('completed', 'Completed')], default='pending'),
        ),
    ]