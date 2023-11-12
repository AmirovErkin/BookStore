from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .models import Book, BlogPostSubscription
from .serializers import BookSerializer, UserSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.filter(is_available=True)
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny,)


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def subscribe(request):
    email = request.data.get('email', None)
    if email:
        subscription = BlogPostSubscription(email=email)
        subscription.save()
        response = {"message": "Assalomu alaykum xurmatli mijoz, siz bizni blog postlarimizga obuna bo’ldingiz va tez orada biz sizga eng yaxshi postlarimizni yuboramiz"}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {"message": "Elektron pochta kerak!"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


