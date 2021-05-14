from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='index'),
    path('about/', views.about, name='about'),
    path('firstpage/', views.page, name='page'),
    path('form/', views.main, name='myform')
]