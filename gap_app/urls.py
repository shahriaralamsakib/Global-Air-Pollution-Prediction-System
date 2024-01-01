from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('register/', views.register, name="registration"),
    path('global_air_polution_predictor/', views.gap, name="gap"),
    path('output/<str:rs>/', views.output, name="output"),
    path('logout/',views.logout_form, name = 'logout'),

]