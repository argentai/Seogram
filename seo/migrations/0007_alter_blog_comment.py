# Generated by Django 3.2.8 on 2021-11-06 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0006_alter_blog_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seo.comment'),
        ),
    ]
