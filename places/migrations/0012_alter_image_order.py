# Generated by Django 5.0.3 on 2024-04-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
