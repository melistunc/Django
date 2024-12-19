from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index") #boş bırakıldığında index'e gitsin.
] 