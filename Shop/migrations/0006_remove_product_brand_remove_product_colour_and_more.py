# Generated by Django 4.1.4 on 2023-04-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_remove_cartitem_added_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='colour',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
        migrations.RemoveField(
            model_name='product',
            name='p_id',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(default='Unavailable', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
