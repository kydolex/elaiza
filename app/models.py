from django.conf import settings
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db.models.fields import TextField
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.decorators import login_required
from stdimage.models import StdImageField
from mdeditor.fields import MDTextField
from markdownx.models import MarkdownxField
from accounts.models import CustomUser


class Post(models.Model):
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	title = models.CharField("タイトル", max_length=200)
	content = models.TextField("本文")
	created = models.DateTimeField("作成日", default=timezone.now)

	def __str__(self):
		return self.title

class Maker(models.Model):
    maker = models.CharField("メーカー名", max_length=200,null=True)
    image = StdImageField(upload_to='images', verbose_name='アイコン',  null=True, blank=True ,variations={
        'size_1': (200, 100, True),
        'size_2': (400, 400),
        'size_3': (600, 600),
        'size_4': (800, 600),
        'size_5': (3000, 2000),
    })
    def __str__(self):
        return self.maker

class Car(models.Model):
    maker = models.ForeignKey(Maker,related_name='maker_key', on_delete=models.CASCADE)
    car = models.CharField("車名", max_length=200,null=True)
    def __str__(self):
        return self.car


class Item(models.Model):
    car = models.ForeignKey(Car,related_name='car_key', on_delete=models.CASCADE)
    name = models.CharField("車名", max_length=200,null=True)
    year = models.CharField("年式　ex) 平成24年6月", max_length=200,null=True)
    syaken = models.CharField("車検　ex) 令和6年6月", max_length=200,null=True)
    distance = models.CharField("走行距離", max_length=200,null=True)
    biko = models.TextField("備考欄", max_length=200,null=True)
    url = models.TextField("ジモティに行くリンク", max_length=200,null=True)
    image = StdImageField(upload_to='images', verbose_name='最初の写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_2 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_3 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_4 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_5 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_6 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_7 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_8 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_9 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_10 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_11 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_12 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_13 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_14 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_15 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_16 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_17 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_18 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_19 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    image_20 = StdImageField(upload_to='images', verbose_name='写真',  null=True, blank=True ,variations={
        'size_1': (400, 400, True),
        'size_2': (1000, 1000),
    })
    def __str__(self):
        return self.name