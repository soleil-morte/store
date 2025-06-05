from django.urls import path
from .views import *
urlpatterns=[
    path('index/',Index),
    path('store/',Store),
    path('productdetail/<int:pk>/', ProductDetail.as_view()),
    path('addproduct/',AddProduct),
    path('contact/',Sms),
    path('categories/',Categories)
]