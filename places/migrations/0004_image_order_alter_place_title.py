# Generated by Django 5.0.3 on 2024-03-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_rename_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название экскурсии'),
        ),
    ]
