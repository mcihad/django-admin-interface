# Generated by Django 4.0.7 on 2022-09-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0025_theme_language_chooser_control"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="list_filter_highlight",
            field=models.BooleanField(default=True, verbose_name="highlight active"),
        ),
    ]
