# Generated by Django 4.1.7 on 2023-02-18 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_rename_models_carmain_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmain',
            old_name='model',
            new_name='models',
        ),
    ]
