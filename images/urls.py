from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.image_create, name="create"),
    path(r"(?P<img>[-\w]+)/$", views.detail, name="detail"),
]
