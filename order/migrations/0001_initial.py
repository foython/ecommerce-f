# Generated by Django 4.2.4 on 2023-11-26 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0002_alter_deliverytype_delivery_price'),
        ('product', '0011_alter_sizeandquantity_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('company_name', models.CharField(blank=True, max_length=128, null=True)),
                ('country', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=256)),
                ('postcode', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('province', models.CharField(max_length=128)),
                ('phone_no', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cupon_code', models.CharField(max_length=10)),
                ('discount_percentage', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], max_length=16)),
                ('total', models.FloatField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.billingaddress')),
                ('delivery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='delivery.deliverytype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField()),
                ('payment_type', models.CharField(blank=True, choices=[('0', 'Paypal'), ('1', 'cash on delievery'), ('2', 'credit card'), ('3', 'direct bank transfer')], default=None, max_length=32, null=True)),
                ('status', models.CharField(blank=True, choices=[('succeed', 'Succeed'), ('sailed', 'Failed'), ('pending', 'Pending')], default=None, max_length=32, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('session', models.CharField(max_length=256)),
                ('size', models.CharField(max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('sub_total', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='order.orderitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
