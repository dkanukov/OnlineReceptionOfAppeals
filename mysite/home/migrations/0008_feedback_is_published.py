# Generated by Django 4.0.8 on 2022-12-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_report_file_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
