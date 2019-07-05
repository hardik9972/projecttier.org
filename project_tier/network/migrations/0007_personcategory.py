# Generated by Django 2.1.8 on 2019-05-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20190504_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField(blank=True, help_text='Lower numbers are shown first. If left blank, it will show up at the end.', null=True)),
            ],
            options={
                'verbose_name': 'People category',
                'verbose_name_plural': 'People categories',
                'ordering': ['order', 'title'],
            },
        ),
    ]