# Generated by Django 4.2.4 on 2023-11-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_type_name', models.CharField(max_length=32)),
                ('delivery_price', models.IntegerField()),
            ],
        ),
    ]
