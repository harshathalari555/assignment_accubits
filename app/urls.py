from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('', viewset=views.BookList)
router.register('author_books', viewset=views.AuthorbooksList)

urlpatterns = [
    path('books/', include(router.urls))
]