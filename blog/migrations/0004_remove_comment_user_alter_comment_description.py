# Generated by Django 5.1.7 on 2025-04-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='description',
            field=models.TextField(help_text='Enter a comment about the post', max_length=1000),
        ),
    ]
