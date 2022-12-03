# Generated by Django 3.2.9 on 2021-11-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('style', models.CharField(max_length=200)),
                ('time_to_prepare', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.CharField(default='', max_length=500)),
                ('ingredients', models.ManyToManyField(to='store.Ingredient')),
            ],
        ),
    ]
