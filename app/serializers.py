from rest_framework import serializers
from app.models import *


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

