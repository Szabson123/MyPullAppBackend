# Generated by Django 5.1.5 on 2025-01-20 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_note_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='note.language'),
        ),
        migrations.AlterField(
            model_name='link',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='note.note'),
        ),
    ]
