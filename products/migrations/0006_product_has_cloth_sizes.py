# Generated by Django 5.0.4 on 2024-04-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_cloth_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
