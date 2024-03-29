# Generated by Django 4.0.4 on 2022-12-02 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(blank=True, max_length=20)),
                ('title_of', models.CharField(blank=True, max_length=20)),
                ('college', models.CharField(blank=True, max_length=20)),
                ('department', models.CharField(blank=True, max_length=20)),
                ('telephone', models.CharField(blank=True, max_length=20)),
                ('coursefield', models.CharField(blank=True, max_length=20)),
                ('specify_course', models.CharField(blank=True, max_length=20)),
                ('department_choice', models.CharField(blank=True, max_length=20)),
                ('year_of_study', models.PositiveIntegerField(blank=True, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=20)),
                ('area_of_residence', models.CharField(blank=True, max_length=20)),
                ('guardian_name', models.CharField(blank=True, max_length=20)),
                ('guardian_number', models.CharField(blank=True, max_length=11)),
                ('intern_picture', models.ImageField(blank=True, upload_to='uploads/')),
                ('student_id_picture', models.ImageField(blank=True, upload_to='uploads/')),
                ('work_type', models.CharField(blank=True, max_length=20)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-university',),
            },
        ),
    ]
