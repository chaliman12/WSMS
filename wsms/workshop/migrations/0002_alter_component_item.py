# Generated by Django 4.2.6 on 2023-10-25 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='workshop.item'),
        ),
    ]