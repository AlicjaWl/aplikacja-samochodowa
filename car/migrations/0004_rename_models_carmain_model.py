# Generated by Django 4.1.7 on 2023-02-18 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_rename_model_carmain_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmain',
            old_name='models',
            new_name='model',
        ),
    ]
