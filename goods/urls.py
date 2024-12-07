from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.catalogView.as_view(), name='search'),
    path('<slug:category_slug>/', views.catalogView.as_view(), name='index'),
    path('product/<slug:product_slug>/', views.productView.as_view(), name='product'),

]
