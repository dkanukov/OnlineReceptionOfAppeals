# Generated by Django 4.0.8 on 2023-01-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='completion_date',
            field=models.DateField(default=None, null=True, verbose_name='Дата выполнения обращения'),
        ),
    ]