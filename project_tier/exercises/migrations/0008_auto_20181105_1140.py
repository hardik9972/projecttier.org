# Generated by Django 2.0.4 on 2018-11-05 16:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('exercises', '0007_exerciseindexpage_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='software_tags_relationship', to='exercises.ExercisePage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises_softwaretag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exercisepage',
            name='software_tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='+', through='exercises.SoftwareTag', to='taggit.Tag', verbose_name='software tags'),
        ),
    ]