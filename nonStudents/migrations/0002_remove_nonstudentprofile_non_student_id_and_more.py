# Generated by Django 4.0.4 on 2023-01-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonStudents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonstudentprofile',
            name='non_student_id',
        ),
        migrations.AddField(
            model_name='nonstudentprofile',
            name='level_of_skill',
            field=models.CharField(choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nonstudentprofile',
            name='program_of_interest',
            field=models.CharField(default='computing', max_length=30),
            preserve_default=False,
        ),
    ]
