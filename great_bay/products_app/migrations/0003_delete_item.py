# Generated by Django 2.2.1 on 2019-05-15 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0003_delete_bid'),
        ('products_app', '0002_item_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]
