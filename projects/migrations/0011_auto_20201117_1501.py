# Generated by Django 3.1.1 on 2020-11-17 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='resume',
            new_name='cvupload',
        ),
    ]
