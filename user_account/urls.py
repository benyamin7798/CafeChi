
from django.urls import path
from .views import (custom_login_view,
                    sign_up_view)
from django.contrib.auth.views import LogoutView

urlpatterns = [
            path('login/',custom_login_view,name='login'),
            path('logout/',LogoutView.as_view(),name='logout'),
            path('signup/',sign_up_view,name='signup'),
]