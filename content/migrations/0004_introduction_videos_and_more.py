# Generated by Django 4.0.4 on 2022-11-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_landing_page_information_first_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction_Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video_link', models.CharField(blank=True, max_length=500, null=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='landing_page_information',
            name='first_video',
        ),
        migrations.RemoveField(
            model_name='landing_page_information',
            name='fourth_video',
        ),
        migrations.RemoveField(
            model_name='landing_page_information',
            name='second_video',
        ),
        migrations.RemoveField(
            model_name='landing_page_information',
            name='third_video',
        ),
    ]
