from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog_list/', views.BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('like_change/<int:pk>/', views.Change_Like.as_view(), name='like_change'),

    path('shop_list/', views.ShopListView.as_view(), name='shop_list'),
    path('shop_detail/<int:pk>/', views.ShopDetailView.as_view(), name='shop_detail'),
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('car_detail/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
]