# Generated by Django 5.0.2 on 2024-03-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(default=1, verbose_name='Дата производства продукта'),
            preserve_default=False,
        ),
    ]
