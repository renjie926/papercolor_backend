# Generated by Django 3.2.25 on 2024-10-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper_app', '0004_auto_20241018_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='color_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]