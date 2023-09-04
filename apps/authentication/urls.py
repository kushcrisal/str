# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view,base,screenlocation,contactus
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', base, name="base"),
    path('contactus/', contactus, name="contactus"),
    path('screenlocation/', screenlocation, name="screenlocation"),
    path('login/', login_view, name="login"),
    
    path("logout/", LogoutView.as_view(), name="logout")
]
