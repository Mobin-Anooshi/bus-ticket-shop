# Generated by Django 5.1 on 2024-08-17 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_diver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='diver',
            new_name='driver',
        ),
    ]
