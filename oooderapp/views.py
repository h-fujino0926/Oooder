from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import path

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

# ここから下画面遷移のためのView
# 変更(削除)予定
class MenuView(TemplateView):
    template_name = 'menu.html'

class cartView(TemplateView):
    template_name = 'cart.html'

class historyView(TemplateView):
    template_name = 'history.html'

class orderView(TemplateView):
    template_name = 'order.html'

class payView(TemplateView):
    template_name = 'pay.html'

class welcomeView(TemplateView):
    template_name = 'welcome.html'

# ここまで画面遷移のためのView