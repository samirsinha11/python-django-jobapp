# Generated by Django 4.1.1 on 2022-09-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_jobpost_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost", name="expiry", field=models.DateField(null=True),
        ),
    ]
