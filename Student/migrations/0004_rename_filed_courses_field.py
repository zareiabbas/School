# Generated by Django 3.2.9 on 2021-11-08 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20211108_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='filed',
            new_name='field',
        ),
    ]