# Generated by Django 3.2.6 on 2023-10-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0010_alter_assignments_completed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='is_valid',
            field=models.BooleanField(auto_created=True, default=True),
        ),
        migrations.AddField(
            model_name='component',
            name='is_valid',
            field=models.BooleanField(auto_created=True, default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='is_valid',
            field=models.BooleanField(auto_created=True, default=True),
        ),
        migrations.AddField(
            model_name='section',
            name='is_valid',
            field=models.BooleanField(auto_created=True, default=True),
        ),
    ]
