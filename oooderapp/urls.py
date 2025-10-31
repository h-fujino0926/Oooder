from djanogo.urls import path
from . import views

app_name = 'oooderapp'

url_patterns = [
    path('', views.IndexView.as_view(), name='index'),
]