# Generated by Django 3.2.6 on 2023-10-09 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0007_alter_users_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='item',
        ),
        migrations.RemoveField(
            model_name='section',
            name='manager',
        ),
        migrations.DeleteModel(
            name='Assignments',
        ),
        migrations.DeleteModel(
            name='Component',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
