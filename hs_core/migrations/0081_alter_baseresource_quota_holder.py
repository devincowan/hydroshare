# Generated by Django 3.2.25 on 2024-05-01 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hs_core', '0080_baseresource_quota_holder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseresource',
            name='quota_holder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quota_holder', to=settings.AUTH_USER_MODEL),
        ),
    ]