# Generated by Django 4.2.7 on 2023-11-06 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_alter_notification_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
