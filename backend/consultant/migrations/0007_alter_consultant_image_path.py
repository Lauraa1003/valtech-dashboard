# Generated by Django 4.1.1 on 2022-11-09 09:36

import consultant.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consultant", "0006_remove_consultant_projects_consultant_unavailable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultant",
            name="image_path",
            field=models.ImageField(
                blank=True, null=True, upload_to=consultant.models.Consultant.upload_to
            ),
        ),
    ]
