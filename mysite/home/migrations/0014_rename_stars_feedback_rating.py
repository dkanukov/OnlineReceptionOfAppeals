# Generated by Django 4.0.6 on 2022-08-31 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_feedback_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='stars',
            new_name='rating',
        ),
    ]
