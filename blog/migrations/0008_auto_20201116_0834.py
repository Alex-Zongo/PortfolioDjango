# Generated by Django 3.1.1 on 2020-11-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200925_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', width_field=100),
        ),
    ]
