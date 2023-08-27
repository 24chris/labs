# Generated by Django 4.0.4 on 2022-10-06 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('level', models.CharField(max_length=30)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('level', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_module', to='course.course')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('level', models.CharField(max_length=30)),
                ('video_url', models.CharField(blank=True, max_length=500, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_lesson', to='course.module')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
