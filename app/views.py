from django.views.generic import View
from django.shortcuts import render
from .models import Post
from .models import Blog_Post,Blog_Comment,Category,ShopCategory,CarCategory
from .models import LikePostAll,LikePost
from accounts.models import CustomUser
from .forms import BlogCommentForm
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse 
from django.utils import timezone
import datetime
from django.core.mail import send_mail, EmailMessage,BadHeaderError
from django.views import generic
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.template.loader import render_to_string
from django.utils.timezone import localtime, make_aware
from django.views.decorators.http import require_POST
import json


class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'post_data': post_data,
        })

class CarListView(View):
    def get(self, request, *args, **kwargs):
        try:
            user_data = CustomUser.objects.get(id=request.user.id)  
        except CustomUser.DoesNotExist:
            user_data = None
        category_data = Category.objects.order_by("id")
        post_data = Blog_Post.objects.order_by("-id")
        post_data_2 = Blog_Post.objects.order_by("?")
        car_data = CarCategory.objects.order_by("-id")
        return render(request, 'app/car_list.html', {
            'user_data':user_data,
            'category_data':category_data,
            'post_data': post_data,
            'post_data_2':post_data_2,
            'car_data':car_data,
        })
class CarDetailView(View):
    def get(self, request, *args, **kwargs):
        try:
            user_data = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            user_data = None
        car_data = CarCategory.objects.order_by("?")
        category = Category.objects.order_by("?")
        header_active_3 = "active"
        car_detail = CarCategory.objects.get(id=self.kwargs['pk'])
        post_data = Blog_Post.objects.order_by("-id").filter(car_category=car_detail.id)
        return render(request, 'app/blog_list.html', {
            'header_active_3':header_active_3,
            'post_data':post_data,
            'user_data':user_data,
            'category':category,
            'car_data':car_data,
            'car_detail':car_detail,
        })

class ShopListView(View):
    def get(self, request, *args, **kwargs):
        try:
            user_data = CustomUser.objects.get(id=request.user.id)  
        except CustomUser.DoesNotExist:
            user_data = None
        category_data = Category.objects.order_by("id")
        post_data = Blog_Post.objects.order_by("-id")
        post_data_2 = Blog_Post.objects.order_by("?")
        shop_data = ShopCategory.objects.order_by("-id")

        return render(request, 'app/shop_list.html', {
            'user_data':user_data,
            'category_data':category_data,
            'post_data': post_data,
            'post_data_2':post_data_2,
            'shop_data':shop_data,
        })
class ShopDetailView(View):
    def get(self, request, *args, **kwargs):
        try:
            user_data = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            user_data = None
        shop_data = ShopCategory.objects.order_by("?")
        category = Category.objects.order_by("?")
        header_active_3 = "active"
        shop_detail = ShopCategory.objects.get(id=self.kwargs['pk'])
        post_data = Blog_Post.objects.order_by("-id").filter(shop_category=shop_detail.id)
        return render(request, 'app/blog_list.html', {
            'header_active_3':header_active_3,
            'post_data':post_data,
            'user_data':user_data,
            'category':category,
            'shop_data':shop_data,
            'shop_detail':shop_detail,
        })

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        try:
            user_data = CustomUser.objects.get(id=request.user.id)  
        except CustomUser.DoesNotExist:
            user_data = None
        category_data = Category.objects.order_by("id")
        post_data = Blog_Post.objects.order_by("-id")
        post_data_2 = Blog_Post.objects.order_by("?")
        return render(request, 'app/blog_list.html', {
            'user_data':user_data,
            'category_data':category_data,
            'post_data': post_data,
            'post_data_2':post_data_2,
        })

class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        try:
            user_data = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            user_data = None
        post_detail = Blog_Post.objects.get(id=self.kwargs['pk'])
        post_data = Blog_Post.objects.order_by("?")
        form = BlogCommentForm(request.POST, request.FILES)
        blog_comment = Blog_Comment.objects.order_by('id')

        post_detail.watch += 1
        post_detail.save()

        like_data =LikePostAll.objects.filter(like= post_detail)
        if LikePostAll.objects.filter(user=user_data,like= post_detail).exists():
            like_data = LikePostAll.objects.get(user=user_data,like= post_detail)

        return render(request, 'app/blog_detail.html', {
            'user_data':user_data,
            'post_detail':post_detail,
            'post_data': post_data,
            'like_data':like_data,
            'blog_comment': blog_comment,
            'form':form,
        })
    def post(self, request, *args, **kwargs):
        try:
            user_data = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            user_data = None
            bloger_category = None
        form = BlogCommentForm(request.POST, request.FILES)
        blog_detail = Blog_Post.objects.get(id=self.kwargs['pk'])
        blog_detail.comment += 1
        blog_detail.save()
        if form.is_valid():
            form_data = Blog_Comment()
            form_data.author = request.user
            form_data.content = form.cleaned_data['content']
            form_data.blog = Blog_Post.objects.get(id=self.kwargs['pk'])
            id = "form_id"
            form_data.save()
            return redirect('blog_detail', self.kwargs['pk'])
        return render(request, 'app/blog_detail.html', {
            'user_data':user_data,
            'bloger_category':bloger_category,
            'form': form,
        })


class Change_Like(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        like = Blog_Post.objects.get(id=self.kwargs['pk'])
        order_item, created = LikePostAll.objects.get_or_create(
            user=user_data,
            like =like,
        )
        order = LikePost.objects.filter(user=user_data)
        if order.exists():
            order = order[0]
            if order.likes.filter(like=like).exists():
                order_item = LikePostAll.objects.filter(
                    like=like,
                    user=user_data,
                )[0]
                order.likes.remove(order_item)
                order_item.delete()
                like.like -= 1
                like.save()
                return JsonResponse({"like":like.like})
            else:
                order.likes.add(order_item)
                like.like += 1
                like.save()
                return JsonResponse({"like":like.like})
        else:
            order = LikePost.objects.create(user=user_data)
            order.likes.add(order_item)
            like.like += 1
            like.save()
        return JsonResponse({"like":like.like})
