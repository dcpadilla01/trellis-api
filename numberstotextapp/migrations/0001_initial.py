# Generated by Django 5.0 on 2023-12-20 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_number', models.IntegerField()),
                ('converted_number', models.CharField(max_length=255)),
            ],
        ),
    ]
