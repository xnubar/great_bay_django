# Generated by Django 2.2.1 on 2019-05-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('start_bid', models.FloatField(default=0.0)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]
