# Generated by Django 4.0.6 on 2022-08-02 04:37

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_likepostall_likepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリ')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='イメージ画像')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリ')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='イメージ画像')),
            ],
        ),
        migrations.AddField(
            model_name='blog_post',
            name='car_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_car', to='app.category', verbose_name='車カテゴリ'),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='shop_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_shop', to='app.category', verbose_name='店カテゴリ'),
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_blog', to='app.category', verbose_name='カテゴリ'),
        ),
    ]
