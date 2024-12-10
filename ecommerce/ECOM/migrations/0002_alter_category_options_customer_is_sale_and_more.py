# Generated by Django 5.1.4 on 2024-12-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ECOM", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "catergories"},
        ),
        migrations.AddField(
            model_name="customer",
            name="is_sale",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customer",
            name="sale_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
