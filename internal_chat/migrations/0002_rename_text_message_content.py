# Generated by Django 5.2.3 on 2025-07-09 08:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("internal_chat", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="text",
            new_name="content",
        ),
    ]
