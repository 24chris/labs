# Generated by Django 4.0.4 on 2023-05-02 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_comment_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='course',
        ),
    ]
