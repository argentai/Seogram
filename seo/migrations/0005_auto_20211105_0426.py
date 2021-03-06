# Generated by Django 3.2.8 on 2021-11-05 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comment',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='seo.comment'),
        ),
        migrations.AddField(
            model_name='blog',
            name='comment_count',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='default', to='seo.Tag'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='blog',
            field=models.ManyToManyField(blank=True, related_name='default', to='seo.Blog'),
        ),
    ]
