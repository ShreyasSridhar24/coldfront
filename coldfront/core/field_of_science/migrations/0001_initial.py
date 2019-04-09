# Generated by Django 2.2 on 2019-04-09 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOfScience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_selectable', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=255)),
                ('fos_nsf_id', models.IntegerField(blank=True, null=True)),
                ('fos_nsf_abbrev', models.CharField(blank=True, max_length=10, null=True)),
                ('directorate_fos_id', models.IntegerField(blank=True, null=True)),
                ('parent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='field_of_science.FieldOfScience')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
    ]
