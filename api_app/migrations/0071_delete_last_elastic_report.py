# Generated by Django 4.2.17 on 2025-02-19 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0070_remove_comment_job_comment_analyzable"),
    ]

    operations = [
        migrations.DeleteModel(
            name="LastElasticReportUpdate",
        ),
    ]
