# Generated by Django 4.1 on 2022-11-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_project", "0002_rename_user_project_userproject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userproject",
            name="date_finished",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userproject",
            name="date_started",
            field=models.DateField(blank=True, null=True),
        ),
    ]
