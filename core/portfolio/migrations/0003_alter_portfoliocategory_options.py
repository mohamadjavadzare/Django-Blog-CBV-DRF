# Generated by Django 4.2.4 on 2023-10-03 21:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_alter_portfoliocategory_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="portfoliocategory",
            options={"verbose_name_plural": "Portfolio Categories"},
        ),
    ]