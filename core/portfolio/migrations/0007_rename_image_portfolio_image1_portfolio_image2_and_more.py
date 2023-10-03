# Generated by Django 4.2.4 on 2023-10-03 23:13

import datetime
from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0006_alter_portfolio_project_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="portfolio",
            old_name="image",
            new_name="image1",
        ),
        migrations.AddField(
            model_name="portfolio",
            name="image2",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="portfolio/",
                validators=[portfolio.models.Portfolio.validate_image],
            ),
        ),
        migrations.AddField(
            model_name="portfolio",
            name="image3",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="portfolio/",
                validators=[portfolio.models.Portfolio.validate_image],
            ),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="project_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 10, 4, 2, 43, 17, 810360)
            ),
        ),
    ]