# Generated by Django 4.0.1 on 2022-07-04 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='cashdevlivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_index=True, max_length=50)),
                ('lastname', models.CharField(db_index=True, max_length=50)),
                ('address', models.CharField(db_index=True, max_length=50)),
                ('contact', models.CharField(db_index=True, max_length=50)),
            ],
            options={
                'db_table': 'Cashdeliverys',
            },
        ),
    ]