# Generated by Django 3.2.6 on 2023-10-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0013_assignments'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_accepted',
            field=models.BooleanField(auto_created=True, default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.IntegerField(choices=[(1, 'pending'), (2, 'On_progress'), (3, 'Completed'), (4, 'Not maintanable')], default=1),
        ),
    ]
