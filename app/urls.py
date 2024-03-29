from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'), 
    path('orverview', views.OverView.as_view(), name='orverview'),
]