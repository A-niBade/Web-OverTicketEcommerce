from django.urls import path, include

from product import views

urlpatterns = [
    path('latest-products/', views.LastestProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]