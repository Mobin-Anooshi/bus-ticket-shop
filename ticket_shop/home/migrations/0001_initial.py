# Generated by Django 5.1 on 2024-08-29 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(choices=[('car', 'CAR'), ('bus', 'BUS'), ('van', 'VAN')], max_length=3)),
                ('number', models.CharField(max_length=8)),
                ('model', models.CharField(max_length=30)),
                ('chair', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('o_d', models.PositiveIntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('destance', models.PositiveIntegerField(default='0')),
                ('valid', models.BooleanField(default=False)),
                ('sell_chair', models.SmallIntegerField(default=0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cars')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.travel')),
            ],
        ),
    ]
