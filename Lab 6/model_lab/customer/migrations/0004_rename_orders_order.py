# Generated by Django 5.0.2 on 2024-02-28 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
