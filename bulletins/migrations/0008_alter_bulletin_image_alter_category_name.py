# Generated by Django 5.0 on 2023-12-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0007_bulletin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='image',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Bulletin Category'),
        ),
    ]
