from core. models import Book, User
from rest_framework import serializers



class BookSerializer(serializers.ModelSerializer):
    reader = serializers.ReadOnlyField(source='reader.username')
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'description', 'featured', 'publication_date', 'reader', 'review',)


class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'books',)