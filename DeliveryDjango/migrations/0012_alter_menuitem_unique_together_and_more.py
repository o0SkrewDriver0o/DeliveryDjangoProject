# Generated by Django 5.2.1 on 2025-05-27 17:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryDjango', '0011_category_alter_dish_category'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menuitem',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='review',
            name='service_quality_rating',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='availability',
            field=models.IntegerField(),
        ),
    ]
