# Generated by Django 4.2.4 on 2023-10-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='sub_title',
        ),
        migrations.AddField(
            model_name='project',
            name='hosted_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]