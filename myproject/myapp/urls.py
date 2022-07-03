from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("form", views.form, name="form"),
    path("counter", views.counter, name="counter")
]
