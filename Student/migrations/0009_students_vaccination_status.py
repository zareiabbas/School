# Generated by Django 3.2.9 on 2021-11-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0008_alter_students_father_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='vaccination_status',
            field=models.CharField(choices=[('Unvaccinated', 'Unvaccinated'), ('First Dose', 'First Dose'), ('Second Dose', 'Second Dose')], default='Unvaccinated', max_length=12),
        ),
    ]
