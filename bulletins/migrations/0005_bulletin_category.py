# Generated by Django 5.0 on 2023-12-12 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0004_remove_bulletin_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bulletin_category', to='bulletins.category'),
            preserve_default=False,
        ),
    ]
