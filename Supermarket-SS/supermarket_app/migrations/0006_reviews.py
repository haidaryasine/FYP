# Generated by Django 3.2.8 on 2023-05-05 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_app', '0005_alter_orderedproduct_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(default='')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket_app.user')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermarket_app.product')),
            ],
        ),
    ]
