# Generated by Django 5.0.7 on 2024-08-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("models", "0005_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
