# Generated by Django 3.2.7 on 2021-09-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('provider', models.CharField(max_length=30)),
                ('name_of_product', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('amount', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
