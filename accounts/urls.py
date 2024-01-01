from django.urls import path,include
from. views import UserRegistrationView,UserLoginView,UserLogoutView,UserBankAccountupdateView,ChangePasswordView

urlpatterns = [
    
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', UserLogoutView.as_view(),name='logout'),
    path('profile/', UserBankAccountupdateView.as_view(),name='profile'),
    path('pass_change/',ChangePasswordView,name='pass_change'),
]
