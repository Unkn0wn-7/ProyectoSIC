# Generated by Django 3.2.8 on 2023-10-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('ide', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=4)),
                ('tipo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
