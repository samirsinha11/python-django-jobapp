# Generated by Django 4.1.1 on 2022-09-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscribe", "0006_alter_subscribe_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscribe",
            name="newsletter",
            field=models.CharField(
                choices=[("M", "Monthly"), ("W", "Weekly")], default="M", max_length=2
            ),
        ),
    ]
