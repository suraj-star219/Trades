from django.urls import include, path
from rest_framework import routers 

from .views import *

from . import views

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view()),
    path('changepassword/',UserChangePasswordView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('registeremail/',RegisterEmail.as_view()),
    path('verifyemail/',VerifyEmailView.as_view()),
    path('registerphone/',views.RegisterPhoneView),
    path('verifyphone/',views.VerifyPhoneView),
    path('bank/',BankView.as_view()),
    path('nominee/',NomineeView.as_view()),
    path('kyc/',UserKYCView.as_view()),
    path('watchlist/', Watchlist_View.as_view()),
    path('orders_create/', Orders_Create.as_view()),
    path('orders_list/', Order_List.as_view()),
    path('order_option/', Order_Option.as_view()),
    path('simple_check/', views.Check),
    path('add_fund/', Add_Fund.as_view()),
    path('portfolio/', Portfolio.as_view()),
    path('checkout/<int:id>', views.checkout),
    path('withdraw/<int:id>', views.withdraw),
    #path('checkout/<int:id>/', views.checkout),
    path('handlerequest/', views.handlerequest),

   
    ]