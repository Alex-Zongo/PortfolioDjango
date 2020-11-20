# Generated by Django 3.1.1 on 2020-11-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20201116_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.RemoveField(
            model_name='project',
            name='report',
        ),
    ]