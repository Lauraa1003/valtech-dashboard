# Generated by Django 4.1 on 2022-11-01 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("skill", "0001_initial"),
        ("consultant", "0001_initial"),
        ("user_project", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="User_project", new_name="UserProject",),
    ]
