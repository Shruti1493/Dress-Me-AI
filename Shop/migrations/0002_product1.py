# Generated by Django 4.1.4 on 2023-04-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('img', models.URLField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
    ]
