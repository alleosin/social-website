from django.urls import path, include

from account import views
# from django.contrib.auth.views import auth_login, auth_logout, logout_then_login

urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),

    # login / logout urls
    # path('login/', auth_login, name='login'),
    # path('logout/', auth_logout, name='logout'),
    # path('logout-then-login/', logout_then_login, name='logout_then_login'),
    path("", views.dashboard, name="dashboard"),
    path("", include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
]