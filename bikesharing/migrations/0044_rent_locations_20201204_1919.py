# Generated by Django 3.1.2 on 2020-12-04 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0043_remove_tracker_type_string_20201120_1738"),
    ]

    operations = [
        migrations.AddField(
            model_name="rent",
            name="end_location",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rent_end_location",
                to="bikesharing.location",
            ),
        ),
        migrations.AddField(
            model_name="rent",
            name="start_location",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rent_start_location",
                to="bikesharing.location",
            ),
        ),
    ]
