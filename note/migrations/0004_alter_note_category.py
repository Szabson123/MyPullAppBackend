# Generated by Django 5.1.5 on 2025-01-21 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_alter_category_language_alter_link_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.category'),
        ),
    ]
