# Generated by Django 4.0.8 on 2023-01-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_appeal_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
