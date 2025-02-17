from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('main-category/<slug:category_slug>/', views.main_category, name='main_category'),
    path('subcategory/<slug:subcategory_slug>/', views.subcategory, name='subcategory'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search_results/', views.search, name='search_results'),
]
