# Generated by Django 5.0.3 on 2024-04-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_alter_place_lat_alter_place_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='Номер изображения'),
        ),
    ]
