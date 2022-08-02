# Generated by Django 4.0.6 on 2022-07-31 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, choices=[('green', '緑'), ('dark', '黒'), ('blue', '青'), ('light-blue', '水色'), ('yellow', '黄色'), ('red', '赤'), ('pink', 'ピンク'), ('orange', 'オレンジ')], max_length=60, null=True, verbose_name='色')),
                ('bg_color', models.CharField(blank=True, choices=[('bg-green', '緑'), ('bg-red', '黒'), ('bg-blue', '青'), ('bg-light-blue', '水色'), ('bg-yellow', '黄色'), ('bg-red', '赤'), ('bg-pink', 'ピンク'), ('bg-orange', 'オレンジ')], max_length=60, null=True, verbose_name='背景色')),
                ('border_color', models.CharField(blank=True, choices=[('border-green', '緑'), ('border-red', '黒'), ('border-blue', '青'), ('border-light-blue', '水色'), ('border-yellow', '黄色'), ('border-red', '赤'), ('border-pink', 'ピンク'), ('border-orange', 'オレンジ')], max_length=60, null=True, verbose_name='線色')),
                ('bg_color_filter', models.CharField(blank=True, choices=[('bg-green-filter', '緑'), ('bg-red-filter', '黒'), ('bg-blue-filter', '青'), ('bg-light-blue-filter', '水色'), ('bg-yellow-filter', '黄色'), ('bg-red-filter', '赤'), ('bg-pink-filter', 'ピンク'), ('bg-orange-filter', 'オレンジ')], max_length=60, null=True, verbose_name='背景色(透け)')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリ')),
                ('content', models.TextField(blank=True, verbose_name='本文')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='イメージ画像')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(blank=True, max_length=200, null=True, verbose_name='キーワード')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('text', models.TextField(blank=True, null=True, verbose_name='アピール文')),
                ('content_1_1', mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='本文')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('like', models.IntegerField(default=0)),
                ('watch', models.IntegerField(default=0)),
                ('comment', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_blog', to='app.category', verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, null=True, verbose_name='コメント')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.blog_post')),
            ],
        ),
    ]
