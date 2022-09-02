# Generated by Django 4.0.6 on 2022-08-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_partner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Partner',
        ),
        migrations.AddField(
            model_name='feedback',
            name='stars',
            field=models.IntegerField(default=5, verbose_name='Количество звезд'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='second_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='дополнительный номер телефона'),
        ),
    ]