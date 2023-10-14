# Generated by Django 4.2.6 on 2023-10-13 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0016_alter_item_is_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.IntegerField(auto_created=True, choices=[(1, 'pending'), (2, 'On_progress'), (3, 'Completed'), (4, 'Not maintanable')], default=1),
        ),
    ]
