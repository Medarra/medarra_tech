# Generated by Django 4.2.1 on 2023-06-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_author_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]