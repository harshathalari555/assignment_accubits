from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('books', viewset=views.BookList)

urlpatterns = [
    path('', include(router.urls))
]