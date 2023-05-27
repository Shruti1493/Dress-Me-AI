# Generated by Django 4.1.4 on 2023-04-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('status', models.CharField(default='Unavailable', max_length=20)),
            ],
        ),
    ]
