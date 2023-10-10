# Generated by Django 3.2.6 on 2023-10-09 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workshop', '0008_auto_20231009_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ws_id', models.CharField(max_length=15)),
                ('received_date', models.DateField(auto_now=True)),
                ('stock_id', models.CharField(max_length=15)),
                ('Serial_no', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('delivered_by', models.CharField(max_length=100)),
                ('received_by', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'pending'), (2, 'accepted'), (3, 'Completed'), (4, 'Not maintanable')], default=1)),
                ('remark', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('is_superuser', models.BooleanField(auto_created=True, blank=True, default=False, null=True)),
                ('is_staff', models.BooleanField(auto_created=True, blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(auto_created=True, default=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_name', models.EmailField(max_length=50, unique=1)),
                ('pass_word', models.CharField(max_length=15)),
                ('user_type', models.IntegerField(choices=[(1, 'manager'), (2, 'registeror'), (3, 'Engineer')], default=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.users')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('recived_date', models.DateField(auto_now=True)),
                ('stock_id', models.CharField(max_length=15)),
                ('Serial_no', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('remark', models.TextField(blank=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.item')),
            ],
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('as_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('remark', models.TextField(blank=True)),
                ('Assigned_date', models.DateField(auto_now=True)),
                ('completed_date', models.DateField(default='2023-11-02')),
                ('Section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.section')),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.users')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workshop.item')),
            ],
        ),
    ]