# Generated by Django 4.2.6 on 2023-10-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0018_component_repeat_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='Repeat_Count',
        ),
        migrations.AddField(
            model_name='item',
            name='Repeat_Count',
            field=models.IntegerField(auto_created=True, default=1),
        ),
    ]
