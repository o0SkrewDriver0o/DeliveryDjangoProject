# Generated by Django 5.2.1 on 2025-05-27 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryDjango', '0012_alter_menuitem_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='availability',
        ),
    ]
