from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializers
from .permissions import IsUserOwnerOrGetAndPostOnly

class UserAPIView(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly]
    
    queryset = User.objects.all()
    serializer_class = UserSerializers