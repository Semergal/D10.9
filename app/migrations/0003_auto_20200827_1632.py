# Generated by Django 3.0.8 on 2020-08-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200827_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[(1, 'Красный'), (2, 'Белый'), (3, 'Черный'), (4, 'Фиолетовый'), (5, 'Синий'), (6, 'Зеленый')], max_length=33, verbose_name='Цвет'),
        ),
    ]
