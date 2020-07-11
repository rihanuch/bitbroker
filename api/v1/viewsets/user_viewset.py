from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import get_user_model

from api.permissions import (
    is_owner
)

from api.v1.serializers.user_serializer import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer
    permission_classes = [
        is_owner.IsUser
    ]

    def list(self, request):
        queryset = User.objects.filter(email=self.request.user.email)
        serializer = UserSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)
