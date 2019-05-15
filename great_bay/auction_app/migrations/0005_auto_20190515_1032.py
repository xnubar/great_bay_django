# Generated by Django 2.2.1 on 2019-05-15 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products_app', '0004_item'),
        ('auction_app', '0004_bid'),
        ('users_app', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='consumer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.Customer'),
        ),
        migrations.AddField(
            model_name='bid',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.Item'),
        ),
    ]