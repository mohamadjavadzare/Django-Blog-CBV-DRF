# Generated by Django 4.2.4 on 2023-10-12 11:41

import blog.formatChecker
import blog.models
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("accounts", "0003_alter_profile_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="blog/default.jpg",
                        upload_to="blog/",
                        validators=[blog.models.Post.validate_image],
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("summary", models.TextField(blank=True)),
                ("content", ckeditor_uploader.fields.RichTextUploadingField()),
                (
                    "audio",
                    blog.formatChecker.ContentTypeRestrictedFileField(
                        blank=True,
                        null=True,
                        upload_to="uploads/",
                        verbose_name="audio",
                    ),
                ),
                (
                    "video",
                    blog.formatChecker.ContentTypeRestrictedFileField(
                        blank=True,
                        null=True,
                        upload_to="uploads/",
                        verbose_name="video",
                    ),
                ),
                (
                    "estimated_time",
                    models.PositiveIntegerField(
                        default=10, verbose_name="Estimated time (minutes)"
                    ),
                ),
                ("counted_views", models.PositiveIntegerField(default=0)),
                ("counted_likes", models.PositiveIntegerField(default=0)),
                ("publish_status", models.BooleanField(default=False)),
                ("published_date", models.DateTimeField(null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.profile",
                    ),
                ),
                ("category", models.ManyToManyField(to="blog.category")),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_date",),
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=70)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("approved", models.BooleanField(default=False)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
            ],
            options={
                "ordering": ("-created_date",),
            },
        ),
    ]
