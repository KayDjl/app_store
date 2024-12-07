from django.urls import path

from main import views

app_name = 'main'
urlpatterns = [
    path('', views.indexView.as_view(), name='index'),
    path('about/', views.aboutView.as_view(), name='about'),
]
