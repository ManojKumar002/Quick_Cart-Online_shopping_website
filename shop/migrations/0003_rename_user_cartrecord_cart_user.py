# Generated by Django 3.2.8 on 2021-11-19 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cartrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartrecord',
            old_name='user',
            new_name='cart_user',
        ),
    ]