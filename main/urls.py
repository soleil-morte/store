from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('index/',Index),
    path('store/',Store),
    path('productdetail/<int:pk>/', ProductDetail.as_view()),
    path('addproduct/',AddProduct),
    path('contact/',Sms),
    path('categories/',Categories),
    path('blog/',Blog),
    path('fullinfo/<int:pk>/',Fullinfo.as_view()),
    path('auth-registration/', Register),
    path('auth-login/', LoginView.as_view()),
    path('logout/', Logout)
]