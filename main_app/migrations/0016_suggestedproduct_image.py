# Generated by Django 5.0.4 on 2024-05-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_product_brand_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestedproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='suggested_products/'),
        ),
    ]