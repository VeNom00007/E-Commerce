# Generated by Django 3.2.9 on 2023-04-22 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20230422_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='app1.product_images'),
        ),
    ]
