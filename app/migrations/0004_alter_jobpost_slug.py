# Generated by Django 4.1.1 on 2022-09-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_jobpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="slug",
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]