# -*- coding: utf-8 -*-
from django.urls import path
from django.contrib import admin  
from . import views
app_name='keeper'
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home,name='home'),
    path('total/', views.total,name='total'),
    path('remove/', views.remove,name='remove'),
    #path('export/', views.export,name='export'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('render/pdf/', views.Pdf.as_view(),name='export'),
    ]
