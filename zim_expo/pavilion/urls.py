from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('main',views.main, name='main'),
    path('footer',views.footer, name='footer'),

    #Nav Urls
    path('tourism/', views.tourism, name='tourism'),
    path('map/', views.map, name='map'),

    # Exhibits
    path('art_craft/', views.art, name='art_craft'),
    path('music/', views.music, name='music'),
    path('interactive/', views.interactive, name='interactive'),

    # Events
    path('schedule/', views.schedule, name='schedule'),  # URL for the schedule page
     path('live_streaming/', views.live, name='live_streaming'),

    # Opportunities
    path('investment/', views.investment, name='investment'),
    path('industries/', views.industries, name='industries'),
    path('partnerships/', views.partnerships, name='partnerships'),

    # News
    path('news/', views.news, name='news'),  # URL for news page

    # Contact
    path('contact/', views.contact, name='contact'),

    # Our Future
     path('future/', views.future, name='future'),

     # Shop
    path('products/', views.shop, name='products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]