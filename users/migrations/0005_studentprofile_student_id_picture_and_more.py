# Generated by Django 4.0.4 on 2022-11-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_studentprofile_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='student_id_picture',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='student_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
