# Generated by Django 4.0.1 on 2022-07-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_product_product_photo_1_product_product_photo_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='medicine',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='skin',
            field=models.BooleanField(default=True),
        ),
    ]