# Generated by Django 4.2.17 on 2025-01-06 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='aproved',
            new_name='approved',
        ),
    ]
