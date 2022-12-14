# Generated by Django 4.1.1 on 2022-11-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consultant", "0007_alter_consultant_image_path"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consultant",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="display_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="edited_time",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="first_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="last_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="office_category",
            field=models.CharField(
                blank=True,
                choices=[("Baden", "Baden"), ("Bern", "Bern"), ("Geneva", "Geneva")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="primary_language",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="role_category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("frontend", "Frontend Developer"),
                    ("backend", "Backend Developer"),
                    ("devops", "DevOps Developer"),
                    ("fullstack", "Fullstack Developer"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="consultant",
            name="username",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
