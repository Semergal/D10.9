# Generated by Django 3.0.8 on 2020-08-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200828_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.SmallIntegerField(choices=[(1, 'Красный'), (2, 'Белый'), (3, 'Черный'), (4, 'Фиолетовый'), (5, 'Синий'), (6, 'Зеленый')], max_length=33, verbose_name='Цвет'),
        ),
    ]
