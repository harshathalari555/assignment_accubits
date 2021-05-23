from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.
class BookList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

@api_view(["POST",])
def register_view(request):
    if request.method =="POST":
        serializer = AccountSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response']= "sussessfully registerd new account"
            data['username']= account.username
            data['password'] = account.password
            data['email'] = account.email
            token = Token.objects.get_or_create(user=account).key
            print(token)
            data['token'] = token
        else:
            serializer.errors

        return Response(data)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)

class AuthorbooksList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('author',)

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

def booklibrary(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'book.html', {'books': books})

def bookdetails(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_details.html', {'book': book})

