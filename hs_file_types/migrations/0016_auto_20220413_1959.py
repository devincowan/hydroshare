# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-13 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import hs_core.hs_rdf


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('hs_file_types', '0015_auto_20220329_2149'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='FieldInformation',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('object_id', models.PositiveIntegerField()),
                        ('fieldName', models.CharField(max_length=128)),
                        ('fieldType', models.CharField(max_length=128)),
                        ('fieldTypeCode', models.CharField(blank=True, max_length=50, null=True)),
                        ('fieldWidth', models.IntegerField(blank=True, null=True)),
                        ('fieldPrecision', models.IntegerField(blank=True, null=True)),
                        ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hs_file_types_fieldinformation_related', to='contenttypes.ContentType')),
                    ],
                    options={
                        'abstract': False,
                    },
                    bases=(models.Model, hs_core.hs_rdf.RDF_Term_MixIn),
                ),
                migrations.CreateModel(
                    name='GeometryInformation',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('object_id', models.PositiveIntegerField()),
                        ('featureCount', models.IntegerField(default=0)),
                        ('geometryType', models.CharField(max_length=128)),
                        ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hs_file_types_geometryinformation_related', to='contenttypes.ContentType')),
                    ],
                    bases=(models.Model, hs_core.hs_rdf.RDF_Term_MixIn),
                ),
                migrations.CreateModel(
                    name='OriginalCoverageGeofeature',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('object_id', models.PositiveIntegerField()),
                        ('northlimit', models.FloatField()),
                        ('southlimit', models.FloatField()),
                        ('westlimit', models.FloatField()),
                        ('eastlimit', models.FloatField()),
                        ('projection_string', models.TextField(blank=True, null=True)),
                        ('projection_name', models.TextField(blank=True, max_length=256, null=True)),
                        ('datum', models.TextField(blank=True, max_length=256, null=True)),
                        ('unit', models.TextField(blank=True, max_length=256, null=True)),
                        ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hs_file_types_originalcoveragegeofeature_related', to='contenttypes.ContentType')),
                    ],
                    bases=(models.Model, hs_core.hs_rdf.RDF_Term_MixIn),
                ),
                migrations.AlterUniqueTogether(
                    name='originalcoveragegeofeature',
                    unique_together=set([('content_type', 'object_id')]),
                ),
                migrations.AlterUniqueTogether(
                    name='geometryinformation',
                    unique_together=set([('content_type', 'object_id')]),
                ),
            ],
            # prevent creating tables in DB - we will using the existing tables originally created for geofeature
            # resource app
            database_operations=[]
        )
    ]