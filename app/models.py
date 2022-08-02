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
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField("タイトル", max_length=200)
	content = models.TextField("本文")
	created = models.DateTimeField("作成日", default=timezone.now)

	def __str__(self):
		return self.title


class ShopCategory(models.Model):
	name = models.CharField("カテゴリ", max_length=50)
	content = models.TextField("本文",null=True, blank=True)
	icon = StdImageField(upload_to='images', verbose_name='アイコン',  null=True, blank=True ,variations={
		'size_1': (200, 100, True),
		'size_2': (400, 400),
		'size_3': (600, 600),
		'size_4': (800, 600),
		'size_5': (3000, 2000),
	})
	image = StdImageField(upload_to='images', verbose_name='イメージ画像',  null=True, blank=True ,variations={
		'size_1': (200, 100, True),
		'size_2': (400, 400),
		'size_3': (600, 600),
		'size_4': (800, 600),
		'size_5': (3000, 2000),
	})
	def __str__(self):
		return self.name

class CarCategory(models.Model):
    name = models.CharField("カテゴリ", max_length=50)
    content = models.TextField("本文",null=True, blank=True)
    image = StdImageField(upload_to='images', verbose_name='イメージ画像',  null=True, blank=True ,variations={
        'size_1': (200, 100, True),
        'size_2': (400, 400),
        'size_3': (600, 600),
        'size_4': (800, 600),
        'size_5': (3000, 2000),
    })
    def __str__(self):
        return self.name

class Category(models.Model):
    COLOR_SELECT = (
        ('green', '緑'),
        ('dark', '黒'),
        ('blue', '青'),
        ('light-blue', '水色'),
        ('yellow', '黄色'),
        ('red', '赤'),
        ('pink', 'ピンク'),
        ('orange', 'オレンジ'),
    )
    BACK_COLOR_SELECT = (
        ('bg-green', '緑'),
        ('bg-red', '黒'),
        ('bg-blue', '青'),
        ('bg-light-blue', '水色'),
        ('bg-yellow', '黄色'),
        ('bg-red', '赤'),
        ('bg-pink', 'ピンク'),
        ('bg-orange', 'オレンジ'),
    )
    BACK_COLOR_SELECT_FILTER = (
        ('bg-green-filter', '緑'),
        ('bg-red-filter', '黒'),
        ('bg-blue-filter', '青'),
        ('bg-light-blue-filter', '水色'),
        ('bg-yellow-filter', '黄色'),
        ('bg-red-filter', '赤'),
        ('bg-pink-filter', 'ピンク'),
        ('bg-orange-filter', 'オレンジ'),
    )
    BORDER_COLOR = (
        ('border-green', '緑'),
        ('border-red', '黒'),
        ('border-blue', '青'),
        ('border-light-blue', '水色'),
        ('border-yellow', '黄色'),
        ('border-red', '赤'),
        ('border-pink', 'ピンク'),
        ('border-orange', 'オレンジ'),
    )
    color = models.CharField(choices=COLOR_SELECT,verbose_name="色",max_length=60,null=True, blank=True)
    bg_color = models.CharField(choices=BACK_COLOR_SELECT,verbose_name="背景色",max_length=60,null=True, blank=True)
    border_color = models.CharField(choices=BORDER_COLOR,verbose_name="線色",max_length=60,null=True, blank=True)
    bg_color_filter = models.CharField(choices=BACK_COLOR_SELECT_FILTER,verbose_name="背景色(透け)",max_length=60,null=True, blank=True)
    name = models.CharField("カテゴリ", max_length=50)
    content = models.TextField("本文",null=False, blank=True)
    image = StdImageField(upload_to='images', verbose_name='イメージ画像',  null=True, blank=True ,variations={
        'size_1': (200, 100, True),
        'size_2': (400, 400),
        'size_3': (600, 600),
        'size_4': (800, 600),
        'size_5': (3000, 2000),
    })
    def __str__(self):
        return self.name


class Blog_Post(models.Model):
	author = models.ForeignKey(CustomUser,null=True, on_delete=models.CASCADE, blank=True)
	category = models.ForeignKey(CarCategory, verbose_name='カテゴリ', on_delete=models.PROTECT,related_name='related_blog',null=True, blank=True)
	shop_category = models.ForeignKey(ShopCategory, verbose_name='店カテゴリ', on_delete=models.PROTECT,related_name='related_shop',null=True, blank=True)
	car_category = models.ForeignKey(Category, verbose_name='車カテゴリ', on_delete=models.PROTECT,related_name='related_car',null=True, blank=True)
	keywords= models.CharField("キーワード", max_length=200,null=True, blank=True)
	title = models.CharField("タイトル", max_length=200)
	text= models.TextField("アピール文",null=True, blank=True)
	content_1_1 = MDTextField("本文",null=True, blank=True)
	created = models.DateTimeField("作成日", default=timezone.now)
	like = models.IntegerField(default=0)
	watch = models.IntegerField(default=0)
	comment = models.IntegerField(default=0) 

	def __str__(self):
		return self.title

class Blog_Comment(models.Model):
    author = models.ForeignKey(CustomUser,null=True, on_delete=models.CASCADE, blank=True)
    blog = models.ForeignKey(Blog_Post, on_delete=models.CASCADE,null=True)
    content = models.CharField("コメント", max_length=200,null=True)
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.blog

class LikePostAll(models.Model):
    user = models.ForeignKey(CustomUser,null=True, on_delete=models.CASCADE, blank=True)
    like = models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.email
        
class LikePost(models.Model):
    user = models.ForeignKey(CustomUser,null=True, on_delete=models.CASCADE, blank=True)
    likes = models.ManyToManyField(LikePostAll)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.email