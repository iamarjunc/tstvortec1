# Generated by Django 5.1.1 on 2024-09-13 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('customer_id', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('fax', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_code', models.CharField(max_length=100, unique=True)),
                ('part_name', models.CharField(max_length=255)),
                ('details', models.TextField(blank=True, null=True)),
                ('material_used', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=100, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('In Progress', 'In Progress'), ('Completed', 'Completed')], default='In Progress', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app1.customer')),
                ('ship_to_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ship_orders', to='app1.customer')),
                ('part_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app1.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_notes', models.TextField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to='app1.order')),
            ],
        ),
    ]
