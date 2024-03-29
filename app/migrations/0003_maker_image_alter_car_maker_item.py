# Generated by Django 4.1.5 on 2023-02-05 06:34

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_maker_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='maker',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='アイコン'),
        ),
        migrations.AlterField(
            model_name='car',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maker_key', to='app.maker'),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='車名')),
                ('year', models.CharField(max_length=200, null=True, verbose_name='年式\u3000ex) 平成24年6月')),
                ('syaken', models.CharField(max_length=200, null=True, verbose_name='車検\u3000ex) 令和6年6月')),
                ('distance', models.CharField(max_length=200, null=True, verbose_name='走行距離')),
                ('biko', models.TextField(max_length=200, null=True, verbose_name='備考欄')),
                ('url', models.TextField(max_length=200, null=True, verbose_name='ジモティに行くリンク')),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='最初の写真')),
                ('image_2', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_3', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_4', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_5', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_6', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_7', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_8', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_9', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_10', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_11', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_12', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_13', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_14', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_15', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_16', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_17', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_18', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_19', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('image_20', stdimage.models.StdImageField(blank=True, null=True, upload_to='images', verbose_name='写真')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_key', to='app.car')),
            ],
        ),
    ]
