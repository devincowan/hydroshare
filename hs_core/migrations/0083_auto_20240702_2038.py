# Generated by Django 3.2.25 on 2024-07-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs_core', '0082_merge_20240509_1646'),
    ]

    operations = [
        # make a field nullable
        migrations.AlterField(
            model_name='baseresource',
            name='resource_federation_path',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name='baseresource',
                    name='resource_federation_path',
                ),
                migrations.AlterIndexTogether(
                    name='resourcefile',
                    index_together={('object_id', 'resource_file')},
                ),
                migrations.RemoveField(
                    model_name='resourcefile',
                    name='fed_resource_file',
                ),
            ],
            # Operations to be performed later on the database.
            database_operations=[
                # migrations.RunSQL(
                #     sql='ALTER TABLE "hs_core_genericresource" DROP COLUMN "resource_federation_path" CASCADE;',
                # ),
                # migrations.RunSQL(
                #     sql='DROP INDEX IF EXISTS "hs_core_resourcefile_object_id_fed_resource_file_15f4618e_idx";',
                # ),
                # migrations.RunSQL(
                #     sql='ALTER TABLE "hs_core_resourcefile" DROP COLUMN "fed_resource_file" CASCADE;',
                # ),
            ],
        ),
    ]