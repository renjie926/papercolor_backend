# Generated by Django 3.2.25 on 2024-10-14 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='examples/')),
                ('paper_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='paper_app.papertype')),
            ],
        ),
    ]
