# Generated by Django 2.2.1 on 2019-05-15 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
        ('auction_app', '0001_initial'),
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='consumer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.Users'),
        ),
        migrations.AddField(
            model_name='bid',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.Item'),
        ),
    ]
