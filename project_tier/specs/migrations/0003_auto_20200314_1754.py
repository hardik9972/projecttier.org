# Generated by Django 2.1.15 on 2020-03-14 21:54

from django.db import migrations, models
import project_tier.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0002_auto_20200229_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='specslandingpage',
            name='protocol_1',
            field=models.URLField(blank=True, help_text='The link to TIER Protocol Specs v 1'),
        ),
        migrations.AddField(
            model_name='specslandingpage',
            name='protocol_2',
            field=models.URLField(blank=True, help_text='The link to TIER Protocol Specs v 1'),
        ),
        migrations.AddField(
            model_name='specslandingpage',
            name='protocol_3',
            field=models.URLField(blank=True, help_text='The link to TIER Protocol Specs v 1'),
        ),
        migrations.AlterField(
            model_name='filepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/heading.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smallest_heading.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))], label='Panel')))])), ('notice', wagtail.core.blocks.StructBlock([('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock([('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))])), ('simple_flow_boxes', project_tier.blocks.SimpleFlowBlockList()), ('detailed_flow_boxes', project_tier.blocks.DetailedFlowBlockList()), ('periodic_boxes', project_tier.blocks.PeriodicBlockList()), ('highlight_block', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='folderpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/heading.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smallest_heading.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))], label='Panel')))])), ('notice', wagtail.core.blocks.StructBlock([('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock([('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))])), ('simple_flow_boxes', project_tier.blocks.SimpleFlowBlockList()), ('detailed_flow_boxes', project_tier.blocks.DetailedFlowBlockList()), ('periodic_boxes', project_tier.blocks.PeriodicBlockList()), ('highlight_block', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='optionalfilepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/heading.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smallest_heading.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))], label='Panel')))])), ('notice', wagtail.core.blocks.StructBlock([('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock([('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))])), ('simple_flow_boxes', project_tier.blocks.SimpleFlowBlockList()), ('detailed_flow_boxes', project_tier.blocks.DetailedFlowBlockList()), ('periodic_boxes', project_tier.blocks.PeriodicBlockList()), ('highlight_block', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='specslandingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/heading.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smallest_heading.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))], label='Panel')))])), ('notice', wagtail.core.blocks.StructBlock([('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock([('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))])), ('simple_flow_boxes', project_tier.blocks.SimpleFlowBlockList()), ('detailed_flow_boxes', project_tier.blocks.DetailedFlowBlockList()), ('periodic_boxes', project_tier.blocks.PeriodicBlockList()), ('highlight_block', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))]))]),
        ),
    ]
