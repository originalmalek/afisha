# Generated by Django 5.0.3 on 2024-03-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_image_options_alter_place_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='places'),
        ),
    ]
