# Generated by Django 4.1.1 on 2022-09-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscribe", "0005_alter_subscribe_newsletter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscribe",
            name="email",
            field=models.EmailField(max_length=100),
        ),
    ]