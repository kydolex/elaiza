from django.views.generic import View
from django.shortcuts import render
from .models import Post,Item
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
from django.views.generic import ListView,DetailView
from django.views import generic

#! ホーム
class IndexView(ListView):
    template_name = 'app/index.html'
    post_data = Post.objects.order_by("-id")
    model = Item
    paginate_by = 12
    ordering = ['-id']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_queryset(self):
            return self.model.objects.all().order_by("-id")

class DetailView(DetailView):
    template_name = 'app/detail.html'
    post_data = Post.objects.order_by("-id")
    model = Item
    paginate_by = 12
    ordering = ['-id']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
#! 概要説明
class OverView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'app/orverview.html', {
            'post_data': post_data,
        })
