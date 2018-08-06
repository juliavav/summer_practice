# Generated by Django 2.0.7 on 2018-07-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cat',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='cat',
            name='sex',
            field=models.CharField(choices=[('Кот', 'Мальчик'), ('Кошка', 'Девочка')], db_column='Sex', max_length=10),
        ),
        migrations.AlterModelTable(
            name='cat',
            table='Cat_Info',
        ),
    ]
