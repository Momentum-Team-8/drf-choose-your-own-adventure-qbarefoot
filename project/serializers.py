from core. models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'description', 'featured', 'publication_date',)