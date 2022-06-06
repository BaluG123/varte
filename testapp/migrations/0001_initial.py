# Generated by Django 3.2.3 on 2022-05-16 13:52

from django.db import migrations, models
import djrichtextfield.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('titleo', models.CharField(blank=True, max_length=1000, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('imageo', models.FileField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('youtube', models.CharField(blank=True, max_length=2000, null=True)),
                ('twitter', models.CharField(blank=True, max_length=1000000, null=True)),
                ('body', djrichtextfield.models.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('source', models.CharField(blank=True, max_length=64, null=True)),
                ('credit_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('status', models.CharField(choices=[('post', 'POST'), ('draft', 'DRAFT')], max_length=6)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]