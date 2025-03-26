from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Document, Tag
from .serializers import DocumentSerializer, DocumentCreateUpdateSerializer, TagSerializer, UserSerializer


# User Login API (JWT Token)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        user_name = request.data.get('username')
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


# Create Document API
class DocumentCreateView(generics.CreateAPIView):
    serializer_class = DocumentCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# Fetch All Documents API with Sorting & Filtering
class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Document.objects.filter()
        tag_id = self.request.query_params.get('tag_id')
        sort_by = self.request.query_params.get('sort_by')

        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)

        if sort_by in ['created', '-created', 'updated', '-updated']:
            queryset = queryset.order_by(sort_by)

        return queryset


# Retrieve Document API
class DocumentDetailView(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update Document API
class DocumentUpdateView(generics.UpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete Document API
class DocumentDeleteView(generics.DestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
