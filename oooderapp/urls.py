from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'oooderapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('cart/', views.cartView.as_view(), name='cart'),
    path('history/', views.historyView.as_view(), name='history'),
    path('order/', views.orderView.as_view(), name='order'),
    path('pay/', views.payView.as_view(), name='pay'),
    path('welcome/', views.welcomeView.as_view(), name='welcome'),
]