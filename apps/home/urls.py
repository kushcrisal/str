# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('dashboard', views.index, name='home'),
    path('uwtc',views.stream_video_uwtc, name='uwtc'),
    path('naxal',views.stream_video_naxal, name='naxal'),
   

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
